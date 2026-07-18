import os
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.clients import clients_bp

OPENVPN_DIR = '/etc/openvpn/certs'

@clients_bp.route('/')
@login_required
def list_clients():
    clients = []
    if os.path.exists(OPENVPN_DIR):
        files = os.listdir(OPENVPN_DIR)
        clients = [f.replace('.ovpn', '').replace('.conf', '') for f in files if f.endswith(('.ovpn', '.conf'))]
    else:
        flash(f"No se encontró el directorio {OPENVPN_DIR}. Asegúrate de que los permisos sean correctos.")
    
    return render_template('clients.html', clients=clients)
