"""
API tests aligned with GeoAlgtrOpenAPI v1.4.4 (ATR-GEO-PC API).

Run against a live server:
  GEOALGTR_API_BASE=http://localhost:8000 pytest -v

Many endpoints return 4xx/5xx when pipelines, files, or Docker are absent;
those responses are still valid per the OpenAPI document.
"""

from __future__ import annotations
import io
from typing import Iterable
from utils import *
from data import *
import pytest
import requests


class TestGetEndpoints:
    def test_get_nic(self) -> None:
        assertion_Get("/api/getNic",instanceType=dict)

    def test_get_channels_status(self) -> None:
       assertion_Get("/api/getchannelsstatus",instanceType=dict)

    def test_get_profiles(self) -> None:
        assertion_Get("/api/getProfiles",instanceType=dict)

    def test_get_labels(self) -> None:
        assertion_Get("/api/Getlabels")

    def test_keep_alive(self) -> None:
        assertion_Get("/api/keepAlive")

    def test_set_search_locations_missing_params(self) -> None:
        assertion_Get("/api/SetSearchLocations",responseCodes=(400,), isJson=False)

    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_set_search_locations_with_params(self) -> None:
        assertion_Get("/api/SetSearchLocations",params=SET_SEARCH_LOCATIONS_PARAMS ,isJson=False)


class TestPostJsonEndpoints:
    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_no_gps_mode(self) -> None:
        assertion_Post("/api/noGpsMode",json=NO_GPS_MODE_JSON)

    # # to do: i need to make a for loop to do all of then and make it parallel
    # #and the triton server should work
    # #and there is needed a profile!
    def test_start_channel(self) -> None:
        assertion_Post("/api/startchannel",json=START_CHANNEL)

    def test_stop_channel(self) -> None:
         assertion_Post("/api/stopchannel",json=STOP_CHANNEL)

    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_send_ts(self) -> None:
        assertion_Post("/api/sendTS")
    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_stop_ts(self) -> None:
        assertion_Post("/api/stopTS")

    def test_set_parameters(self) -> None:
        assertion_Post("/api/setParameters",json=SET_PARAMETERS)
    
    def test_get_parameters(self) -> None:
        assertion_Post("/api/getParameters",json=GET_PARAMETERS)

#         # i think that i need to assert that i get the parameters of the channelId 1
    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_add_detector(self) -> None:
        assertion_Post("/api/addDetector", json=ADD_DETECTOR)
    # i need to check with mayyan 

    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_remove_detector(self) -> None:
        assertion_Post("/api/removeDetector", json=REMOVE_DETECTOR)


    def test_remove_profile(self,) -> None:
        assertion_Post("/api/removeProfile",json=REMOVE_PROFILE)

    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_pixel2geo(self) -> None:
        assertion_Post("/api/pixel2geo",json=PIXEL2GEO)

    @pytest.mark.skip(reason="Missing required query parameter: \'server_id\' (returns 400)")
    def test_geo2pixel(self) -> None:
        assertion_Post("/api/geo2pixel",json=GEO2PIXEL)

    @pytest.mark.skip(reason="(returns 500)")
    def test_restart_protrack(self) -> None:
        assertion_Post("/api/restartProtrack",json=RESTART_PORTRACK)
 
    def test_set_labels(self) -> None:
        assertion_Post("/api/Setlabels",json=SET_LABELS)

    @pytest.mark.skip(reason="not allowed (returns 405)")
    def test_set_sahi_config(self) -> None:
        assertion_Post("/api/SetSahiConfig",json=SET_SAHI_CONFIG)
    
    def test_remove_profile(self,) -> None:
        assertion_Post("/api/removeProfile",json=REMOVE_PROFILE)

    def test_restart_neuronic_server(self) -> None:
        restartNeuronicServer("/api/restartNeuronicServer")

    @pytest.mark.skip(reason="endpoint not yet implemented on server (returns 404)")
    def test_restart_channel(self) -> None:
        assertion_Post("/api/restartChannel", json=RESTART_CHANNEL)

class TestMultipartEndpoints:
    def test_get_selected_files(self) -> None:
        selectedFiles("/api/getSelectedFiles")
