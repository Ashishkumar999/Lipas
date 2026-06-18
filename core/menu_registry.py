from core.network_discovery import network_discovery

from scanner.header_analyzer import analyze_headers

from scanner.tech_detector import detect_technology

from scanner.service_detector import detect_service

from core.asset_viewer import asset_viewer

from core.asset_details import asset_details

from core.dashboard import dashboard


MENU_REGISTRY = {

    "2": network_discovery,

    "3": analyze_headers,

    "5": detect_technology,

    "20": detect_service,

    "56": asset_viewer,

    "57": asset_details,

    "58": dashboard

}
