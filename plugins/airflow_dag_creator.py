"""
Licensed Materials - Property of IBM
[PID GOES HERE]
Copyright IBM Corp. 2009, 2016
US Government Users Restricted Rights- Use, duplication or disclosure restricted by GSA ADP Schedule
Contract with IBM Corp.
"""
import os

from airflow.plugins_manager import AirflowPlugin
from airflow import configuration
from airflow.www.app import csrf

from flask import Blueprint, request, jsonify
from flask_admin import BaseView, expose

import logging


dags_folder = configuration.get('core', 'DAGS_FOLDER')

class DagCreator(BaseView):
    @expose('/')
    def index(self):
        return self.render(
            "dag_creator/index.html"
        )

    @expose('/create_dag', methods=["POST"])
    @csrf.exempt
    def create_dag(self):
        dag_name: str = request.form.get('dag_name')
        if not dag_name:
            raise Exception(f"Dag name not defined. Supplied args were {request.form}")
        if not dag_name.endswith('.py'):
            dag_name += '.py'

        dag_definition = request.form.get('dag_definition')
        if not dag_definition:
            raise Exception("No dag definition provided")

        logging.info(f"Creating dag {dag_name}")
        dag_location = os.path.join(dags_folder, dag_name)

        if os.path.isfile(dag_location):
            raise Exception("Dag already exists!")

        with open(dag_location, 'w') as dag_file:
            print(dag_definition, file=dag_file)
        return '', 204


dag_cretor_view = DagCreator(category="Admin", name="Create Dag")


dag_creator_bp = Blueprint(
    "dag_creator_bp",
    __name__,
    template_folder='templates',
    static_folder='static',
)


class DAG_Creator_Plugin(AirflowPlugin):
    name = "dag_creator"
    operators = []
    flask_blueprints = [dag_creator_bp]
    hooks = []
    executors = []
    admin_views = [dag_cretor_view]
    menu_links = []