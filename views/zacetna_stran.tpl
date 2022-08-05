%rebase('base.tpl')
  <div class="d-flex justify-content-between align-items-end">
    <div class="invisible"> </div>
    <div class="p-4"> <h1>MATRIČNI KALKULATOR</h1> </div>
    <div class="p-4">
    <form method="POST" action="/odjava/">
    <button type="submit" class="btn btn-outline-primary"> Odjavi se </button>
    </form>
    </div>
  </div>
  <div class="d-flex flex-column">
  <div class="px-4">Dobrodošli! Tu je seznam vaših matrik:</div>
   <div class="px-0">
    <ul>
    <div class="container">
     <div class="row row-cols-auto">
    % for id_matrike, matrika in enumerate(matrike):
      <div class="col px-5 py-3">
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
      </div>
    </div>
    </ul>
    </div> 
    </div>
    <div class="d-flex flex-row-reverse">  
    <div class="p-4 align-self-end"><a href="/odstrani-matriko/">Odstrani matriko </a> </div>
    <div class="p-4 align-self-end"><a href="/dodaj-matriko/">Dodaj matriko </a> </div>
    <div class="p-4 me-auto">
      <form action="/izberi_stevilo/" method="POST">
           <button type="submit" class="btn btn-primary  btn-block" name="izbira" value="ena" >
            Operacije na eni matriki
           </button>
           <button type="submit" class="btn btn-primary  btn-block" name="izbira" value="dve" >
            Operacije na dveh matrikah
           </button>
      </form>
    </div>
    </div>


     
     