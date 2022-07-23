import os
import glob
import itertools as itt
from pathlib import Path
import PyPDF2 as PDF

def main():
    # VERIFICANDO OS ARQUIVOS NA PASTA 'IN' SRC
    files = [i for i in glob.glob('in/*.pdf')]
    
    # DEFININDO OS ARQUIVOS EM VARIAVIES FRENTE E VERSO
    ft = files[0]
    vs = files[1]
    # VERIFICANDO SE EXISTE ARQUIVO COM ESTES FINAIS.
    #print(files[0].endswith("D-FRENTE.pdf"))
    #print(files[1].endswith("D-VERSO.pdf"))

    # DEFININDO UMA VARIAVEL SAIDA COM O PDFFILEWRITER
    pdf_out = PDF.PdfFileWriter()
    # VERIFICANDO SE A VARIAVEL FT EXISTE E SE É UM ARQUIVO VÁLIDO
    if os.path.isfile(ft) and os.path.isfile(vs) == True:
        # ABRINDO O ARQUIVO FT
        with open(ft,'rb') as _impar:
            # ABRINDO O ARQUIVO VS
            with open(vs,'rb') as _par:
                fname = vs.split('.')[0]
                
                # VENDO OS ARQUIVOS ABERTOS
                pdf_impar = PDF.PdfFileReader(_impar)
                pdf_par = PDF.PdfFileReader(_par)

                # INTERANDO SOBRE OS ARQUIVOS
                for p in itt.chain.from_iterable(
                    # CASO QUEIRA COLOCAR ORDEM INVERSA USE reversed(pdf_par.pages)
                      # itt.zip_longest(pdf_impar.pages, reversed(pdf_par.pages)
                        itt.zip_longest(pdf_impar.pages, pdf_par.pages
                        )):
                    if p:
                        # ADICIONANDO AS PAGINAS
                        pdf_out.addPage(p)
                # CRIANDO O ARQUIVO FINAL

                with open(fname+"-MARGED.pdf", 'wb') as f_out:
                    # GRAVANDO O ARQUIVO
                    pdf_out.write(f_out)

                    # MSG DE TERMINO
                    print(f"Arquivo {fname} - CRIADO COM SUCESSO ")


main()
