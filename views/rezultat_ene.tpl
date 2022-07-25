%rebase('base.tpl')
    <h1>MATRIČNI KALKULATOR</h1>
    Dobrodošli!
    Tu je seznam vaših matrik:
    <ul>
    <div class="container ">
     <div class="row row-cols-4">
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
    <div class="col"> <a href="/dodaj-matriko/">Dodaj matriko </a> </div>
     </div>
    </div>
    <div class="d-flex">
       <div class="p-2"> 
        <select name="matrike"  class="custom-select" disabled>
        %for id_matrike in range(len(matrike)):
          %if id_matrike==id_matrike_izbrana:
        <option value="{{ id_matrike }}" selected="selected">Matrika {{id_matrike + 1}}</option>
         %else:
          <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
          %end
        %end
        </select>
        </div>
        <div class="p-2">
        <button type="submit" class="btn btn-primary" disabled>Izberi operacijo </button>
        </div>
        <div class="ml-auto p-2"><a href="/operacije-ena/"> Izberi drugo matriko </a></div>
        </div>
        <div class="row">
         <div class="col">
        <div class="btn-toolbar" role="toolbar" aria-label="Toolbar with button groups">
         <div class="btn-group mr-2" role="group" aria-label="First group">
         <p>
          % for operacija in operacije:
         <button type="button" data-bs-toggle="collapse" data-bs-target="#{{ operacija }}_rezultat" aria-expanded="false" aria-controls="{{ operacija }}_rezultat" class="btn btn-outline-primary" >{{operacija.capitalize()}}</button>
          %end
        %if stopnja!='p':
          <div class="input-group">
            <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence" size="2" value={{ stopnja }} >
            <button type="button" class="btn btn-outline-primary btn-md" data-bs-toggle="collapse" data-bs-target="#potenciraj_rezultat" aria-expanded="false" aria-controls="potenciraj_rezultat" >Potenciraj</button>
            </div>
        %else:
        <form method="POST" action="/potenciraj_rezultat/{{id_matrike_izbrana}}/">
        <div class="input-group">
        <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence" size="2"  >
        <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="potenciraj" >Potenciraj</button>
        </div>
        </form>
        %end
        %if skalar!='s':
        <div class="input-group">
        <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2" value={{ skalar }}>  
        <button type="button" class="btn btn-outline-primary btn-md" data-bs-toggle="collapse" data-bs-target="#mnozenje_s_skalar_rezultat" aria-expanded="true" aria-controls="mnozenje_s_skalar_rezultat">
        Pomnoži
        </button>
        %else:
        <form method="POST" action="/mnozenje_s_skalar_rezultat/{{id_matrike_izbrana}}/">
        <div class="input-group">
        <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2">  
        <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="mnozenje_s_skalar">
        Pomnoži
        </button>
        </div> 
        </form>
        %end
        </div>
         </p>
        </div>
        </div>
        </div>
    <div class="container">
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="transponiraj_rezultat">
                <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika">                                    
                            % for vrstica in  matrika.spremeni_obliko_matrike(): 
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                        </table>
                        </div>
                        <div class="col-sm-auto"> T </div>
                        <div class="col-sm-auto justify-content-sm-center"> = </div>
                        <div class="col-md-auto">
                        <table class="matrika"> 
                            % for vrstica in  transponirana.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                        </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="prirejenka_rezultat">
                <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika">                                     
                            % for vrstica in  matrika.spremeni_obliko_matrike(): 
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                            </table>
                        </div>
                        <div class="col-sm-auto">Prirejenka:</div>
                        <div class="col-sm-auto">
                        <table class="matrika"> 
                            % for vrstica in  prirejenka.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                            </table>
                        </div>
                    </div>
                </div>
            </div>
         </div>
        </div>
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="inverz_rezultat">
                <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika">                                     
                            % for vrstica in  matrika.spremeni_obliko_matrike(): 
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                            </table>
                        </div>
                        <div class="col-sm-auto"> -1 </div>
                        <div class="col-sm-auto justify-content-sm-center"> = </div>
                        <div class="col-sm-auto"> 
                        <table class="matrika"> 
                            % for vrstica in  inverz.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="det_rezultat">
                <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="det">                                   
                            % for vrstica in  matrika.spremeni_obliko_matrike(): 
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                            </table>
                        </div>
                        <div class="col-sm-auto justify-content-sm-center"> = </div>
                        <div class="col-sm-auto justify-content-sm-center"> {{ determinanta }} </div>
                    </div>
                </div>
            </div>
         </div>
        </div>
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="sled_rezultat">
                <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika"                                 
                        % for vrstica in  matrika.spremeni_obliko_matrike(): 
                            <tr>
                            % for element in vrstica:
                            <td>    {{ element }}  </td>
                            % end
                            </tr>
                        % end
                        </table>
                        </div>
                        <div class="col-sm-auto justify-content-sm-center">sled :</div>
                        <div class="col-sm-auto justify-content-sm-center"> {{ sled }}</div>
                    </div>
                </div>
            </div>
        </div>
        </div>
        </div>
        %if stopnja!='p':
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="potenciraj_rezultat">
                <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                            <table class="matrika">                                   
                                % for vrstica in  matrika.spremeni_obliko_matrike():
                                    <tr>
                                    % for element in vrstica:
                                    <td>    {{ element }}  </td>
                                    % end
                                    </tr>
                                % end
                                </table>
                        </div>
                        <div class="col-sm-auto"> {{ stopnja }} </div>
                        <div class="col-sm-auto justify-content-sm-center"> = </div>
                        <div class="col-md-auto">
                            <table class="matrika">                                    
                                % for vrstica in  rezultat_potenciranja.spremeni_obliko_matrike():
                                    <tr>
                                    % for element in vrstica:
                                    <td>    {{ element }}  </td>
                                    % end
                                    </tr>
                                % end
                            </table> 
                        </div>
                    </div>
                </div>
            </div>
          </div>
        </div>
        %end
        %if skalar!='s':
        <div class="row">
                <div class="col">
                     <div class="collapse multi-collapse" id="mnozenje_s_skalar_rezultat">
                       <div class="card card-body">
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-sm-auto justify-content-sm-center">{{ skalar }}</div>
                        <div class="col-md-auto">
                        <table class="matrika">                                   
                            % for vrstica in  matrika.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                        </table>
                        </div>
                        <div class="col-sm-auto justify-content-sm-center"> = </div>
                        <div class="col-md-auto">
                        <table class="matrika">                                    
                            % for vrstica in  rezultat_mnozenjas.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                            </table> 
                        </div>
                     </div>
                 </div>
             </div>
         </div>
     </div>
     %end
    </div>
