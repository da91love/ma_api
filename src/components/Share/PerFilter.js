import React, { useContext } from "react";
import _ from "lodash";
import { MDBInputGroup, MDBInput } from "mdbreact";
import {FILTER_TYPE} from '../../consts/model';
import {MSG} from '../../consts/message';
import {DANGER} from '../../consts/alert';
import AlertContext from "../../contexts/AlertContext";

const PerFilter = (props) => {
    const {title, mdlFilterStatus, setMdlFilterStatus} = props;
    const {alertState,setAlertState} = useContext(AlertContext);

    const minFilterHandler = (value) => {
        // Validation
        // TODO
        if(_.isNaN(parseInt(value))){
            setAlertState({
                eventType: DANGER, //ここでSUCCESS,WARNING,DANGERを選択
                eventMessage: MSG.NAN,
                eventCount: alertState.eventCount + 1,
             });
        } else {
            setMdlFilterStatus({...mdlFilterStatus, [FILTER_TYPE.PER_MIN]:parseInt(value)})
        }
    }

    const maxFilterHandler = (value) => {
        // Validation
        // TODO
        if(_.isNaN(parseInt(value))){
            setAlertState({
                eventType: DANGER, //ここでSUCCESS,WARNING,DANGERを選択
                eventMessage: MSG.NAN,
                eventCount: alertState.eventCount + 1,
             });
        } else {
            setMdlFilterStatus({...mdlFilterStatus, [FILTER_TYPE.PER_MAX]:parseInt(value)})
        }
    }

    return (
        <div className="mt-3">
            <p className="grey-text text-left">
                {title?title:"PER"}
            </p>
            <MDBInputGroup
                material
                containerClassName="m-2"
                inputs={
                <>
                    <MDBInput noTag className="pr-2" type="text" hint="Min" onChange={e => minFilterHandler(e.target.value)}/>
                    <MDBInput noTag className="pl-2" type="text" hint="Max" onChange={e => maxFilterHandler(e.target.value)}/>
                </>
                }
            />
        </div>
    );
};

export default PerFilter;