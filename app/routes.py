from flask import Blueprint, flash, render_template, request, redirect, url_for
from .forms import CadastroClienteForm
from .models import Cliente, db

# Criar um blueprint com um nome único
bp_main = Blueprint('main', __name__)

# Rota da página inicial
@bp_main.route('/')
def index():
    return render_template('index.html')

# Rota para cadastrar um novo cliente
@bp_main.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastro_cliente():
    form = CadastroClienteForm()
    if form.validate_on_submit():
        # Obter os dados do formulário
        nome = form.nome.data
        endereco = form.endereco.data
        telefone = form.telefone.data
        cpf = form.cpf.data
        email = form.email.data
        senha = form.senha.data

        # Verificar se o CPF já está cadastrado no banco de dados
        if Cliente.query.filter_by(cpf=cpf).first():
            flash('CPF já cadastrado. Utilize outro CPF.', 'error')
            return redirect(url_for('main.cadastro_cliente'))

        # Salvar os dados do cliente no banco de dados
        novo_cliente = Cliente(nome=nome, endereco=endereco, telefone=telefone, cpf=cpf, email=email, senha=senha)
        db.session.add(novo_cliente)
        db.session.commit()  # Adicionar o commit aqui para salvar os dados no banco de dados

        # Redirecionar para a página de login com uma mensagem de sucesso
        flash('Cadastro realizado com sucesso. Faça login para continuar.', 'success')
        return redirect(url_for('main.login'))

    return render_template('cadastro_cliente.html', form=form)

# Rota para login do host
@bp_main.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica de autenticação do host (a ser implementada)
    return redirect(url_for('main.busca_cliente'))

# Rota para buscar clientes por nome ou CPF
@bp_main.route('/busca_cliente', methods=['GET', 'POST'])
def busca_cliente():
    resultados = None

    if request.method == 'POST':
        # Obter o termo de busca do formulário
        termo_busca = request.form['termo_busca']

        # Realizar a busca na tabela de clientes
        resultados = Cliente.query.filter(
            (Cliente.nome.like(f'%{termo_busca}%')) | (Cliente.cpf == termo_busca)
        ).all()

    return render_template('busca_cliente.html', resultados=resultados)