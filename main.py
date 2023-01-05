def btnInserir_Click(self):
        nome = self.varNome.get().strip()
        email = self.varEmail.get().strip()

        reNome = re.fullmatch(r"\b[A-Za-z ]+\b", nome)
        reEmail = re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", email)

        if reNome is None:
            self.varResultado.set("Campo nome obrigatório!!")
            self.lblResultado.configure(background="#ff0000")
            self.txtNome.focus()
        elif reEmail is None:
            self.varResultado.set("Campo email obrigatório!!")
            self.lblResultado.configure(background="#ff0000")
            self.txtNome.focus()
        else:
            try:
                conexao = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    password = "",
                    database = "crud_clientes"
                )
                mycursor = conexao.cursor()
                sql = "INSERT INTO clientes (nome,email) VALUES (%s,%s)"
                val = (nome,email)
                mycursor.execute(sql,val)
                conexao.commit()
                self.varResultado.set("Registro inserido com sucesso!!")
                self.lblResultado.configure(background="#3cb371")
            except:
                self.varResultado.set("Erro ao inserir registro!!")
                self.lblResultado.configure(background="#ff0000")