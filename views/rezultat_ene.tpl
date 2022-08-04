%rebase('base.tpl')
    <h1>MATRIČNI KALKULATOR</h1>

    Tu je seznam vaših matrik:
    <div class="float-end p-4">
    <form method="POST" action="/odjava/">
    <button type="submit" class="btn btn-outline-primary"> Odjavi se </button>
    </form>
    </div>
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
    <div class="float-end p-4"> <a href="/">Začetna stran </a> </div> <br>
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
        %if stopnja=='p' and rezultat_potenciranja=='':
            %if skalar!='':
                <form method="POST" action="/operacija-ena/0/{{id_matrike_izbrana}}/n/{{skalar}}/">
                <div class="input-group">
                <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence" size="2"  >
                <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="potenciraj" >Potenciraj</button>
                </div>
                </form>
            %else:
                <form method="POST" action="/operacija-ena/0/{{id_matrike_izbrana}}/n/s/">
                <div class="input-group">
                <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence" size="2"  >
                <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="potenciraj" >Potenciraj</button>
                </div>
                </form>
            %end
         %else:
          %if stopnja!='':
          <div class="input-group">
            <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence"  size="2" value={{ stopnja }}  readonly>
            <button type="button" class="btn btn-outline-primary btn-md " data-bs-toggle="collapse" data-bs-target="#potenciraj_rezultat" aria-controls="potenciraj_rezultat" >Potenciraj</button>
            </div>
          %else:
          <div class="input-group">
            <input type="text"  name="stopnja_potence"  placeholder="Stopnja potence"  size="2"  readonly>
            <button type="button" class="btn btn-outline-primary btn-md " data-bs-toggle="collapse" data-bs-target="#potenciraj_rezultat" aria-controls="potenciraj_rezultat" >Potenciraj</button>
            </div>
          %end
        %end
        %if skalar=='s' and rezultat_mnozenjas=='':
          %if stopnja!='':
            <form method="POST" action="/operacija-ena/0/{{id_matrike_izbrana}}/{{stopnja}}/n/">
            <div class="input-group">
            <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2">  
            <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="mnozenje_s_skalar">
            Pomnoži
            </button>
            </div> 
            </form>
          %else:
             <form method="POST" action="/operacija-ena/0/{{id_matrike_izbrana}}/p/n/">
            <div class="input-group">
            <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2">  
            <button type="submit" class="btn btn-outline-primary btn-md" name="operacija" value="mnozenje_s_skalar">
            Pomnoži
            </button>
            </div> 
            </form>
          %end
        %else:
           %if skalar!='':
            <div class="input-group">
            <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2" value={{ skalar }} readonly>  
            <button type="button" class="btn btn-outline-primary btn-md" data-bs-toggle="collapse" data-bs-target="#mnozenje_s_skalar_rezultat" aria-controls="mnozenje_s_skalar_rezultat">
            Pomnoži
            </button>
           %else:
            <div class="input-group">
            <input type="text" name="zeljen_skalar"  placeholder="Skalar"  size="2"  readonly>  
            <button type="button" class="btn btn-outline-primary btn-md" data-bs-toggle="collapse" data-bs-target="#mnozenje_s_skalar_rezultat" aria-controls="mnozenje_s_skalar_rezultat">
            Pomnoži
            </button>
          %end
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
                    <div class="row justify-content-md-center gx-4">
                      <div class="col-md-auto">
                      <div class="row gx-2">
                        <div class="col-md-auto align-self-start">
                        <table class="matrika">                                    
                            % for vrstica in  matrika_izbrana.spremeni_obliko_matrike(): 
                                <tr>
                                % for element in vrstica:
                                <td>    {{ element }}  </td>
                                % end
                                </tr>
                            % end
                        </table>
                        </div>
                        <div class="col-sm-auto align-self-start"> T </div>
                        <div class="col-sm-auto align-self-center">
                         =
                        </div>
                        </div>
                        </div>
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
                        %if transponirana not in matrike:
                        <div class="col-md-auto">
                        <div class="float-end">
                        <form action="/operacija-ena/1/{{ id_matrike_izbrana }}/{{ stopnja }}/{{ skalar }}/" method="POST">
                        <button type="submit" class="btn btn-light">Shrani rezultat v seznam mojih matrik  </button>
                        </form>
                        </div><br>
                        </div>
                        %end
                    </div>
                </div>
            </div>
        </div>
        </div>
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="prirejenka_rezultat">
                <div class="card card-body">
                %if napake.get("prirejenka")!=None:
                    <div class="alert alert-warning" role="alert">
                   {{ napake["prirejenka"]}}
                    </div>
                %else:
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika">                                     
                            % for vrstica in  matrika_izbrana.spremeni_obliko_matrike(): 
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
                        %if prirejenka not in matrike:
                        <div class="col-md-auto">
                        <p class="float-end">
                        <form action="/operacija-ena/2/{{ id_matrike_izbrana }}/{{ stopnja }}/{{ skalar }}/" method="POST">
                        <button type="submit" class="btn btn-light">Shrani rezultat v seznam mojih matrik  </button>
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
            <div class="collapse multi-collapse" id="inverz_rezultat">
                <div class="card card-body">
                %if napake.get("inverz")!=None:
                 <div class="alert alert-warning" role="alert">
                   {{ napake["inverz"]}}
                 </div>
                %else:
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika">                                     
                            % for vrstica in  matrika_izbrana.spremeni_obliko_matrike(): 
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
                        %if inverz not in matrike:
                        <div class="col-md-auto">
                        <p class="float-end">
                        <form action="/operacija-ena/3/{{id_matrike_izbrana}}/{{ stopnja }}/{{ skalar }}/" method="POST">
                        <button type="submit" class="btn btn-light">Shrani rezultat v seznam mojih matrik  </button>
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
            <div class="collapse multi-collapse" id="det_rezultat">
                <div class="card card-body">
                %if napake.get("det")!=None:
                 <div class="alert alert-warning" role="alert">
                   {{ napake["det"]}}
                 </div>
                %else:
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="det">                                   
                            % for vrstica in  matrika_izbrana.spremeni_obliko_matrike(): 
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
                %end
                </div>
            </div>
         </div>
        </div>
        <div class="row">
         <div class="col">
            <div class="collapse multi-collapse" id="sled_rezultat">
                <div class="card card-body">
                %if napake.get("sled")!=None:
                 <div class="alert alert-warning" role="alert">
                   {{ napake["sled"]}}
                 </div>
                %else:
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                        <table class="matrika"                                 
                        % for vrstica in  matrika_izbrana.spremeni_obliko_matrike(): 
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
                %end
                </div>
            </div>
        </div>
        </div>
        </div>
        %if stopnja!='p' or (stopnja=='p' and rezultat_potenciranja !=''):
        <div class="row">
         <div class="col">
            <div class="collapse show multi-collapse" id="potenciraj_rezultat">
                <div class="card card-body">
                %if napake.get("potenciraj")!=None:
                 <div class="alert alert-warning" role="alert">
                   {{ napake["potenciraj"]}}
                 <form method="POST" action="/operacija-ena/0/{{ id_matrike_izbrana}}/p/{{ skalar }}/">
                     <button type="submit" class="btn btn-link">Ponovno izberi stopnjo </button>
                 </form>
                 </div>
                %else:
                    <div class="row justify-content-md-center gx-3">
                        <div class="col-md-auto">
                            <table class="matrika">                                   
                                % for vrstica in  matrika_izbrana.spremeni_obliko_matrike():
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
                        %if rezultat_potenciranja not in matrike:
                        <div class="col-md-auto">
                        <form action="/operacija-ena/4/{{ id_matrike_izbrana }}/{{ stopnja }}/{{ skalar }}/" method="POST">
                        <button type="submit" class="btn btn-light">Shrani rezultat v seznam mojih matrik  </button>
                        </form>
                        </div>
                        %end
                        <div class="col-md-auto text-right">
                        <form method="POST" action="/operacija-ena/0/{{ id_matrike_izbrana}}/p/{{ skalar }}/">
                                <button type="submit" class="btn btn-link">Izberi drugo stopnjo </button>
                        </form>
                        </div>
                    </div>
                %end
                </div>
            </div>
          </div>
        </div>
        %end
        %if skalar!='s' or (skalar=='s' and rezultat_mnozenjas!= ''):
        <div class="row">
                <div class="col">
                     <div class="collapse show multi-collapse" id="mnozenje_s_skalar_rezultat">
                       <div class="card card-body">
                        %if napake.get("skalar")!=None:
                        <div class="alert alert-warning" role="alert">
                        {{ napake["skalar"]}}
                        <form method="POST" action="/operacija-ena/0/{{ id_matrike_izbrana}}/{{ stopnja }}/s/">
                        <button type="submit" class="btn btn-link">Ponovno izberi skalar</button>
                        </form>
                        </div>
                        %else:
                            <div class="row justify-content-md-center gx-3">
                                <div class="col-sm-auto justify-content-sm-center">{{ skalar }}</div>
                                <div class="col-sm-auto justify-content-sm-center">*</div>
                                <div class="col-md-auto">
                                <table class="matrika">                                   
                                    % for vrstica in  matrika_izbrana.spremeni_obliko_matrike():
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
                                %if rezultat_mnozenjas not in matrike:
                                <div class="col-md-auto">
                                <p class="float-end">
                                <form action="/operacija-ena/5/{{ id_matrike_izbrana }}/{{ stopnja }}/{{ skalar }}/" method="POST">
                                <button type="submit" class="btn btn-light">Shrani rezultat v seznam mojih matrik  </button>
                                </form>
                                </p>
                                </div>
                                %end
                                <div class="col-md-auto text-right">
                                <form method="POST" action="/operacija-ena/0/{{ id_matrike_izbrana}}/{{ stopnja }}/s/">
                                <button type="submit" class="btn btn-link">Izberi drug skalar
                                </button>
                                </form>
                                </div>
                            </div>
                        %end
                 </div>
             </div>
         </div>
     </div>
     %end
    </div>
