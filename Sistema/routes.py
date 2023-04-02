from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import pandas as pd
from Sistema import app

@app.route('/')
def home():
    return render_template('base.html')


@app.route('/inicial', methods=['POST'])
def inicial():
    tabela_usuarios = pd.read_excel("Sistema/tabelas/usuarios.xlsx")
    tabela_turmas = pd.read_excel("Sistema/tabelas/turmas.xlsx")
    tamanho_tbturmas = len(tabela_turmas)
    usuario = request.form['usuario']
    senha = request.form['senha']
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario and str(tabela_usuarios['senha'][i]) == senha:
            idres = tabela_usuarios['id'][i]
            return render_template('inicial.html', usuario=usuario, tabela_usuarios=tabela_usuarios, tabela_turmas=tabela_turmas, idres=idres, tamanho_tbturmas=tamanho_tbturmas)
            break
    else:
        return render_template('erro.html', usuario=usuario)


@app.route('/<usuario>/turma_301')
def turma_301(usuario):
    tabela_usuarios = pd.read_excel('Sistema/tabelas/usuarios.xlsx')
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario:
            alunos_301 = pd.read_excel('Sistema/tabelas/alunos_301.xlsx')
            tamanho_alunos_301 = len(alunos_301)
            turma = '301'
            return render_template('turma_301.html', usuario=usuario, alunos_301=alunos_301, tamanho_alunos_301=tamanho_alunos_301, turma=turma)
            break
        else:
            return "Você não tem permissão para acessar esta página."


@app.route('/<usuario>/turma_302')
def turma_302(usuario):
    tabela_usuarios = pd.read_excel('Sistema/tabelas/usuarios.xlsx')
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario:
            alunos_302 = pd.read_excel('Sistema/tabelas/alunos_302.xlsx')
            tamanho_alunos_302 = len(alunos_302)
            turma = '302'
            return render_template('turma_302.html', usuario=usuario, alunos_302=alunos_302, tamanho_alunos_302=tamanho_alunos_302, turma=turma)
            break
        else:
            return "Você não tem permissão para acessar esta página."


@app.route('/<usuario>/turma_303')
def turma_303(usuario):
    tabela_usuarios = pd.read_excel('Sistema/tabelas/usuarios.xlsx')
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario:
            alunos_303 = pd.read_excel('Sistema/tabelas/alunos_303.xlsx')
            tamanho_alunos_303 = len(alunos_303)
            turma = '303'
            return render_template('turma_303.html', usuario=usuario, alunos_303=alunos_303, tamanho_alunos_303=tamanho_alunos_303, turma=turma)
            break
    else:
        return "Você não tem permissão para acessar esta página."


@app.route('/<usuario>/turma_304')
def turma_304(usuario):
    tabela_usuarios = pd.read_excel('Sistema/tabelas/usuarios.xlsx')
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario:
            alunos_304 = pd.read_excel('Sistema/tabelas/alunos_304.xlsx')
            tamanho_alunos_304 = len(alunos_304)
            turma = '304'
            return render_template('turma_304.html', usuario=usuario, alunos_304=alunos_304, tamanho_alunos_304=tamanho_alunos_304, turma=turma)
            break
        else:
            return "Você não tem permissão para acessar esta página."


@app.route('/<usuario>/turma_305')
def turma_305(usuario):
    tabela_usuarios = pd.read_excel('Sistema/tabelas/usuarios.xlsx')
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario:
            alunos_305 = pd.read_excel('Sistema/tabelas/alunos_305.xlsx')
            tamanho_alunos_305 = len(alunos_305)
            turma = '305'
            return render_template('turma_305.html', usuario=usuario, alunos_305=alunos_305, tamanho_alunos_305=tamanho_alunos_305, turma=turma)
            break
        else:
            return "Você não tem permissão para acessar esta página."


@app.route('/<usuario>/turma_306')
def turma_306(usuario):
    tabela_usuarios = pd.read_excel('Sistema/tabelas/usuarios.xlsx')
    for i in range(len(tabela_usuarios)):
        if tabela_usuarios['usuario'][i] == usuario:
            alunos_306 = pd.read_excel('Sistema/tabelas/alunos_306.xlsx')
            tamanho_alunos_306 = len(alunos_306)
            turma = '306'
            return render_template('turma_306.html', usuario=usuario, alunos_306=alunos_306, tamanho_alunos_306=tamanho_alunos_306, turma=turma)
            break
        else:
            return "Você não tem permissão para acessar esta página."


@app.route('/enviado/<turma>', methods=['POST'])
def enviado(turma):

    enviar_dados = pd.read_excel(f'Sistema/tabelas/alunos_{turma}.xlsx')
    data = request.form['data']
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    data_br = data_obj.strftime("%d/%m/%Y")
    presenca = []
    for i in range(len(enviar_dados)):
        estado_presente = request.form[enviar_dados['nome'][i]]
        presenca.append(estado_presente)
    enviar_dados.loc[:, data_br] = presenca
    enviar_dados.to_excel(f'Sistema/tabelas/alunos_{turma}.xlsx', index=False)
    return render_template('enviado.html')


