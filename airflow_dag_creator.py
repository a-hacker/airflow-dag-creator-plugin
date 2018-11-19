"""
Licensed Materials - Property of IBM
[PID GOES HERE]
Copyright IBM Corp. 2009, 2016
US Government Users Restricted Rights- Use, duplication or disclosure restricted by GSA ADP Schedule
Contract with IBM Corp.
"""
from airflow.plugins_manager import AirflowPlugin
from airflow import configuration

from flask import Blueprint
from flask_admin import BaseView, expose

import logging


class DagCreator(BaseView):
    @expose('/')
    def index(self):
        logging.info("REST_API.index() called")
        return self.render(
            "dag_creator/index.html"
        )


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
    admin_views = []
    menu_links = []
