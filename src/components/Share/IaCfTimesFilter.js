import React, { useContext } from "react";
import _ from "lodash";
import { MDBInputGroup } from "mdbreact";
import {FILTER_TYPE} from '../../consts/model';
import {MSG} from '../../consts/message';
import {DANGER} from '../../consts/alert';
import AlertContext from "../../contexts/AlertContext";

const IaCfTimesFilter = (props) => {
    const {title, mdlFilterStatus, setMdlFilterStatus} = props;
    const {alertState,setAlertState} = useContext(AlertContext);

    const filterHandler = (value) => {
        // Validation
        // TODO
        if(_.isNaN(parseInt(value))){
            setAlertState({
                eventType: DANGER, //ここでSUCCESS,WARNING,DANGERを選択
                eventMessage: MSG.NAN,
                eventCount: alertState.eventCount + 1,
             });
        } else {
            setMdlFilterStatus({...mdlFilterStatus, [FILTER_TYPE.IA_CF_TIMES]:parseInt(value)})
        }
    }

    return (
        <div className="mt-3">
            <p className="grey-text text-left">
                {title?title:"Investment CF ratio"}
            </p>
            <MDBInputGroup
                onChange={e => filterHandler(e.target.value)}
                material
                hint={mdlFilterStatus[FILTER_TYPE.IA_CF_TIMES]}
                containerClassName="mt-0"
                append="% higher than"
            />
        </div>
    );
};

export default IaCfTimesFilter;