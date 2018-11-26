import React from 'react';
import ReactDom from 'react-dom';

class DagForm extends React.Component {
    render(){
        return (
            <form>
                <input type="text" name="dag_id"/>
                <textarea name="dag_definition"/>
                <input type="submit" value="Create Dag"/>
            </form>)
    }
}

ReactDom.render(<DagForm/>, document.getElementById('create_dag'));