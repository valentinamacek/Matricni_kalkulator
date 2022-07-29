%rebase('base.tpl')
    <h1>MATRIČNI KALKULATOR</h1>
    Dobrodošli!
    Tu je seznam vaših matrik:
    <div class="float-end p-4">
    <form method="POST" action="/odjava/">
    <button type="submit" class="btn btn-outline-primary"> Odjavi se </button>
    </form>
    </div>
    <ul>
    <div class="container ">
     <div class="row row-cols-4 ">
    % for id_matrike, matrika in enumerate(matrike):
      <div class="col">
      <li>   Matrika {{ id_matrike + 1 }}:
      <table class="matrika">
      % for vrstica in  matrika.spremeni_obliko_matrike():
          <tr>
          % for element in vrstica:
          <td>    {{ element }}  </td>
          % end
          </tr>
      % end
      </table> 
      </li>
      </div>
    % end
    </ul>
    <div class="float-start p-4">  <a href="/dodaj-matriko/">Dodaj matriko </a> </div> <br>
     </div>
    </div>
      <form action="/izberi_stevilo/" method="POST">
           <button type="submit" class="btn btn-primary  btn-block" name="izbira" value="ena" >
            Operacije na eni matriki
           </button>
           <button type="submit" class="btn btn-primary  btn-block" name="izbira" value="dve" >
            Operacije na dveh matrikah
           </button>
      </form>


     
     