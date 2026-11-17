from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.chamado_model import ChamadoModel

chamado_bp = Blueprint("chamados", __name__)
model = ChamadoModel()

@chamado_bp.route("/", methods=["GET"])
def index():
    filtro = request.args.get("status", "Todos")
    chamados = model.listar_todos(filtro)
    return render_template("index.html", chamados=chamados, filtro_atual=filtro)

@chamado_bp.route("/chamados", methods=["POST"])
def criar_chamado():
    cliente = request.form.get("cliente", "")
    equipamento = request.form.get("equipamento", "")
    defeito = request.form.get("defeito", "")
    prioridade = request.form.get("prioridade", "Média")

    try:
        model.criar(cliente, equipamento, defeito, prioridade)
        flash("Ordem de serviço registrada com sucesso!", "success")
    except ValueError as erro:
        flash(str(erro), "danger")

    return redirect(url_for("chamados.index"))

@chamado_bp.route("/chamados/<int:chamado_id>/status", methods=["POST"])
def alterar_status(chamado_id):
    novo_status = request.form.get("status", "")
    try:
        model.atualizar_status(chamado_id, novo_status)
        flash("Status atualizado com sucesso!", "success")
    except ValueError as erro:
        flash(str(erro), "danger")
    return redirect(url_for("chamados.index"))

@chamado_bp.route("/chamados/<int:chamado_id>/excluir", methods=["POST"])
def excluir_chamado(chamado_id):
    model.excluir(chamado_id)
    flash("Chamado removido com sucesso.", "info")
    return redirect(url_for("chamados.index"))
