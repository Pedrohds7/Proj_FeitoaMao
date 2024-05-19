from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class CadastroClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=100)])
    endereco = StringField('Endereço', validators=[DataRequired(), Length(max=200)])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(max=20)])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(max=100)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, max=100)])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), Length(min=8, max=100), EqualTo('senha', message='As senhas devem ser iguais')])
    submit = SubmitField('Cadastrar')
