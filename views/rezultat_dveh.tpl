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
        <select name="matrika1" class="custom-select" disabled>
        %for id_matrike in range(len(matrike)):
           %if id_matrike==id_matrike1:
          <option value="{{ id_matrike }}" selected="selected">Matrika {{id_matrike + 1}}</option>
           %else:
          <option value="{{ id_matrike }}">Matrika {{id_matrike + 1}}</option>
          %end
        %end
        </select>
        </div>
        <div class="p-2">
        <select name="matrika2" class="custom-select" disabled>
        %for id_matrike in range(len(matrike)):
          %if id_matrike==id_matrike2:
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
        <div class="ml-auto p-2"><a href="/operacije-dve/"> Izberi drugi matriki </a></div>
        </div>
          <p>
          <button type="button" data-bs-toggle="collapse" data-bs-target="#sestej_rezultat" aria-expanded="false" aria-controls="sestej_rezultat" class="btn btn-outline-primary">Seštej</button>
           <button type="button" data-bs-toggle="collapse" data-bs-target="#zmnozi_rezultat" aria-expanded="false" aria-controls="zmnozi_rezultat" class="btn btn-outline-primary">Zmnoži </button>
          </p>
       <div class="container">
        <div class="row">
         <div class="col">
           <div class="collapse multi-collapse" id="sestej_rezultat">
            <div class="card card-body">
              %if napake.get("vsota")!=None:
                 <div class="alert alert-warning" role="alert">
                   {{ napake["vsota"]}}
                 </div>
              %else:
                  <div class="row justify-content-md-center gx-3 ">
                    <div class="col-md-auto">
                        <table class="matrika">                                     
                        % for vrstica in  matrika1.spremeni_obliko_matrike(): 
                            <tr>
                            % for element in vrstica:
                            <td>    {{ element }}  </td>
                            % end
                            </tr>
                        % end
                        </table>
                    </div>
                   <div class="col-sm-auto justify-content-sm-center"> + </div>
                   <div class="col-md-auto">
                      <table class="matrika"> 
                            % for vrstica in  matrika2.spremeni_obliko_matrike():
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
                            % for vrstica in  vsota.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                     </table>
                    </div>
                    %if vsota not in matrike:
                    <div class="col-md-auto">
                    <p class="float-end">
                    <form action="/dodaj-rezultats/{{ id_matrike1 }}/{{ id_matrike2 }}/" method="POST">
                                              <div class="form-check">
                          <input class="form-check-input" type="checkbox" value="" id="shranis">
                          <label class="form-check-label" for="shranis">
                            Shrani rezultat v seznam mojih matrik
                          </label>
                        </div>
                      <button type="submit" class="btn btn-light">Shrani  </button>
                    </form>
                    </p>
                    </div>
                    %end
                  </div>
              %end
            </div>
           </div>
          </div>
          </div>
          <div class="row">
           <div class="col">
            <div class="collapse multi-collapse" id="zmnozi_rezultat">
                <div class="card card-body">
                  %if napake.get("produkt")!=None:
                  <div class="alert alert-warning" role="alert">
                    {{ napake["produkt"] }}
                  </div>
                  %else:
                      <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto ">
                            <table class="matrika">                                     
                              % for vrstica in  matrika1.spremeni_obliko_matrike(): 
                                  <tr>
                                  % for element in vrstica:
                                  <td>    {{ element }}  </td>
                                  % end
                                  </tr>
                              % end
                            </table>
                        </div>
                        <div class="col-sm-auto justify-content-sm-center "> * </div>
                        <div class="col-md-auto">
                          <table class="matrika"> 
                          % for vrstica in  matrika2.spremeni_obliko_matrike():
                              <tr>
                              % for element in vrstica:
                              <td>    {{ element }}  </td>
                              % end
                              </tr>
                          % end
                          </table>
                        </div>
                        <div class="col-sm-auto  justify-content-sm-center"> = </div>
                        <div class="col-md-auto ">
                          <table class="matrika"> 
                            % for vrstica in  produkt.spremeni_obliko_matrike():
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                          </table>
                        </div>
                            %if produkt not in matrike:
                            <div class="col-md-auto offset-md-4">
                            <form action="/dodaj-rezultatz/{{ id_matrike1 }}/{{ id_matrike2 }}/" method="POST">
                                                      <div class="form-check">
                                  <input class="form-check-input" type="checkbox" value="" id="shrani">
                                  <label class="form-check-label" for="shrani">
                                    Shrani rezultat v seznam mojih matrik
                                  </label>
                                </div>
                              <button type="submit" class="btn btn-light"> Shrani  </button>
                            </form>
                            </div>
                            %end
                      </div>
                  %end
                </div>
              </div>
            </div>
          </div>
      </div>