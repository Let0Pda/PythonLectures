from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import pressure_view


def create(device=1):
    xml = (
        '<xml>\n'
        + f'    <temperature units = "c">{temperature_view(device)}</temperature>\n'
    )
    xml += f'    <wind_speed_view units = "m/s">{wind_speed_view(device)}</wind_speed_view>\n'
    xml += f'    <pressure units = "mmHg">{pressure_view(device)}</pressure>\n'
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml


def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n' + f'    <temperature units = "f">{t}</temperature>\n'
    xml += f'    <wind_speed_view units = "m/s">{w}</wind_speed_view>\n'
    xml += f'    <pressure units = "mmHg">{p}</pressure>\n'
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)

    return data
    