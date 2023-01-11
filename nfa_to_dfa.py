import math
import collections
import copy 
import graphviz
####################gprahiz testing#############
# dot = graphviz.Digraph(comment='The Round Table')
# dot.node('A', 'King Arthur')  # doctest: +NO_EXE
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false',label="0")
# # print(dot.source)
# # doctest_mark_exe()
# dot.render('doctest-output/round-table.gv', view=True)  # doctest: +SKIP
# 'doctest-output/round-table.gv.pdf'

##########fucntion defnittions##################
# def get_epslin_closrue(element,nfa_table,alphates,br):
#     stateS=[]
#     index_of_alpha=0
#     while index_of_alpha<br:
#         get_element=nfa_table[element][alphates[index_of_alpha]]
#         if get_element>=0:
#             stateS.append(copy.deepcopy(nfa_table[get_element]['ε'])) 
#             index_of_alpha+=1
#         elif get_element<0:
#             stateS.append([-1])
#             index_of_alpha+=1
#     return stateS
# def remove_all_instances(LisT,item_to_remove):
#     return [i for i in LisT if i!=item_to_remove]
###########################tables###################
# table={0:{'a':-1,'ε':[0,1,3]},1:{'a':2,'ε':[1]},2:{'a':-1,'ε':[1,2,3]},3:{'a':-1,'ε':[3]}}
# table={0:{'a':1,'b':-1,'c':3, 'ε':[0]},1:{'a':-1,'b':2,'c':-1,'ε':[0,1]},2:{'a':1,'b':-1,'c':-1,'ε':[2]},3:{'a':-1,'b':-1,'c':2,'ε':[2,3]}}
table={0:{'0':1,'1':-1, 'ε':[0]},1:{'0':2,'1':4,'ε':[1]},2:{'0':-1,'1':3,'ε':[2]},3:{'0':-1,'1':-1,'ε':[0,3]},
4:{'0':5,'1':-1,'ε':[0,4]},5:{'0':-1,'1':-1,'ε':[0,5]}}

# table={0:{'a':1,'b':-1, 'ε':[0]},1:{'a':2,'b':4,'ε':[1]},2:{'a':-1,'b':3,'ε':[2]},3:{'a':-1,'b':-1,'ε':[0,3]},
# 4:{'a':5,'b':-1,'ε':[0,4]},5:{'a':-1,'b':-1,'ε':[0,5]}}

#########################################

############################################
alpha=['0','1']
# # alpha=['a','b']
# # alpha=['a','b','c']
# # alpha=['a']
##########################
# new_states_flag=0
# dfa_table=dict()
# breakpoint=len(alpha)
# new_states_only=[copy.deepcopy(table[0]['ε'])]
# no_of_lists_to_workon=1
# index_of_current_item=0
# state_number_string='0'
# counter=0

# while(new_states_flag!=1):
#     dicotnray_of_current_item=dict()
#     items_of_alpha=[]
#     for i in range(len(alpha)):
#         dicotnray_of_current_item[alpha[i]]=[]
#     if index_of_current_item==len(new_states_only):
#         new_states_flag=1
#     else:
#         for i in range(len(new_states_only[index_of_current_item])):
#             if i == 0:
#                 current_state_transition=get_epslin_closrue(new_states_only[index_of_current_item][i],table,alpha,breakpoint)
#                 for j in range(len(current_state_transition)):
#                     items_of_alpha.append(current_state_transition[j])
#                     # print("j",j)
#                 indcies_of_items_to_append_to_skip_unique_list=[]
#                 # print(items_of_alpha)
#                 if i==len(new_states_only[index_of_current_item])-1:
#                     # print("hellp")
#                     for li in range(len(items_of_alpha)):
#                         items_of_alpha[li]=remove_all_instances(items_of_alpha[li],-1)
#                     actual_number_of_items_to_append=len(items_of_alpha)
#                     for new_lists_index in range(len(items_of_alpha)):
#                         print(items_of_alpha[new_lists_index])
#                         if sorted(list(set(items_of_alpha[new_lists_index]))) in new_states_only or sorted(list(set(items_of_alpha[new_lists_index]))) == []:
#                             actual_number_of_items_to_append-=1
#                             indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)
          
#                     if actual_number_of_items_to_append==0  and no_of_lists_to_workon==0:
                        
#                         new_states_flag=1
#                     else:
#                         for letter_index in range(len(dicotnray_of_current_item)):
#                             dicotnray_of_current_item[alpha[letter_index]]=sorted(list(set(items_of_alpha[letter_index])))
#                             # state_number_int=int(state_number_string)
#                         dfa_table['S'+state_number_string]=dicotnray_of_current_item
#                         state_number_string=int(state_number_string)+1
#                         state_number_string=str(state_number_string)
#                         for new_lists in range(len(items_of_alpha)):
#                             if new_lists not in indcies_of_items_to_append_to_skip_unique_list:
#                                 new_states_only.append(sorted(list(set(items_of_alpha[new_lists]))))
#                                 no_of_lists_to_workon+=1

#             elif i>0:
#                 index_of_current_letter_toappend=0
#                 current_state_transition=get_epslin_closrue(new_states_only[index_of_current_item][i],table,alpha,breakpoint)
                
#                 for j in range(len(current_state_transition)):
#                     items_of_alpha[index_of_current_letter_toappend].extend(current_state_transition[j])
#                     index_of_current_letter_toappend+=1
              
#                 indcies_of_items_to_append_to_skip_unique_list=[]
#                 if i==len(new_states_only[index_of_current_item])-1:
#                     # print("hellp")
#                     for li in range(len(items_of_alpha)):
#                         items_of_alpha[li]=remove_all_instances(items_of_alpha[li],-1)
#                     actual_number_of_items_to_append=len(items_of_alpha)
#                     for new_lists_index in range(len(items_of_alpha)):
#                         # print(items_of_alpha[new_lists_index])
#                         if sorted(list(set(items_of_alpha[new_lists_index]))) in new_states_only or sorted(list(set(items_of_alpha[new_lists_index]))) == []:
#                             actual_number_of_items_to_append-=1
#                             indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)
                   
#                     if actual_number_of_items_to_append==0 and no_of_lists_to_workon==0:
#                         # print("hellp")
#                         new_states_flag=1
#                     else:
#                         for letter_index in range(len(dicotnray_of_current_item)):
#                             dicotnray_of_current_item[alpha[letter_index]]=sorted(list(set(items_of_alpha[letter_index])))
#                             # state_number_int=int(state_number_string)
#                         dfa_table['S'+state_number_string]=dicotnray_of_current_item
#                         state_number_string=int(state_number_string)+1
#                         state_number_string=str(state_number_string)
#                         for new_lists in range(len(items_of_alpha)):
#                             # print(items_of_alpha[new_lists])
#                             if new_lists not in indcies_of_items_to_append_to_skip_unique_list:
#                                 new_states_only.append(sorted(list(set(items_of_alpha[new_lists]))))
#                                 no_of_lists_to_workon+=1
#                                 # counter+=1
                   
#         index_of_current_item+=1
#         no_of_lists_to_workon-=1


# print(dfa_table)

###################################################

#####################
class dfa_nfa:
    def __init__(self,table=0,alpha=0):
        if table==0:
            self.table=dict()
            self.alpha=0
            self.breakpoint=0

        else:
            self.table=table
            self.alpha=alpha
            self.breakpoint=len(alpha)
        self.dfa_table=dict()
    def get_epslin_closrue(self,element,nfa_table,alphates,br):
        stateS=[]
        index_of_alpha=0
        while index_of_alpha<br:
            get_element=nfa_table[element][alphates[index_of_alpha]]
            if get_element>=0:
                stateS.append(copy.deepcopy(nfa_table[get_element]['ε'])) 
                index_of_alpha+=1
            elif get_element<0:
                stateS.append([-1])
                index_of_alpha+=1
        return stateS
    def remove_all_instances(self,LisT,item_to_remove):
        return [i for i in LisT if i!=item_to_remove]
    def show_nfa_repsenration_(self,nfa_table,breakpoint,alpha):
        dot = graphviz.Digraph(comment='NFA')
        for i in nfa_table.keys():
            # print(i)
            dot.node(str(i), str(i))  # doctest: +NO_EXE
        # dot.node('B', 'Sir Bedevere the Wise')
        # dot.node('L', 'Sir Lancelot the Brave')
        # for i in 
        # dot.edges(['AB', 'AL'])
        # dot.edge('B', 'L', constraint='false',label="0")
        # # print(dot.source)
        # # doctest_mark_exe()
        # dot.render('doctest-output/round-table.gv', view=True)
    # def convert_to_dfa(self,nfa_table,alphates,breakpoint,)
    def genreate_nfa(self):
        self.noofstate=eval(input("enter no of states"))
        self.alpha=[]
        self.noofalpha=eval(input("enter no of alpha"))
        for i in range(self.noofalpha):
            self.letter=input("enter letter")
            self.alpha.append(self.letter)
        for i in range(self.noofstate):
            self.table[i]={}
        self.breakpoint=self.noofalpha
        self.index=0
        for i in self.table:
            self.counter=0
            while(self.counter<=self.breakpoint):
                if self.index==self.breakpoint:
                    self.table[i]["ε"]=[]
                    self.index=0
                    self.counter+=1
                    # print(counter)
                else:
                    self.table[i][self.alpha[self.index]]=""
                    self.index+=1
                    self.counter+=1
                    # print(counter)
        print(self.table)
        for i in self.table:
            self.counter=0
            self.index=0
            self.flag=0
            while(self.counter<=self.breakpoint):
                if self.counter==self.breakpoint:
                    while(self.flag==0):
                        # print("iam here")
                        self.eps_values=int(input("enter epslion closure states"))
                        if self.eps_values>=self.noofstate:
                             return "cannot continue vslue for current letter doendt exist (out of bounds state)"
                        else:
                            self.table[i]['ε'].append(self.eps_values)
                            print("continnue input closures states:")
                            self.choice=input("enter choice")
                        if self.choice=='yes':
                            continue
                        else:
                            self.table[i]['ε']=sorted(list(set(self.table[i]['ε'])))
                            self.counter+=1
                            self.flag=1
                        self.current_state_in=0
                        if i not in self.table[i]['ε']:
                            return "current state not in epslion "
                else:
                    self.charcter=self.alpha[self.index]
                    self.value=int(input("enter value for "+self.charcter+":"))
                    if int(self.value)>=self.noofstate:
                        return "cannot continue vslue for current letter doendt exist (out of bounds state)"
                    else:
                        self.table[i][self.alpha[self.index]]=self.value
                        self.index+=1
                        self.counter+=1

    def convert_to_dfa(self,nfa_table,alpha,breakpoint):
        new_states_flag=0
        self.dfa_table=dict()
        # breakpoint=len(alpha)
        new_states_only=[copy.deepcopy(nfa_table[0]['ε'])]
        no_of_lists_to_workon=1
        index_of_current_item=0
        state_number_string='0'
        counter=0
        while(new_states_flag!=1):
            dicotnray_of_current_item=dict()
            items_of_alpha=[]
            for i in range(len(alpha)):
                dicotnray_of_current_item[alpha[i]]=[]
            if index_of_current_item==len(new_states_only):
                new_states_flag=1
            else:
                for i in range(len(new_states_only[index_of_current_item])):
                    if i == 0:
                        current_state_transition=self.get_epslin_closrue(new_states_only[index_of_current_item][i],nfa_table,alpha,breakpoint)
                        for j in range(len(current_state_transition)):
                            items_of_alpha.append(current_state_transition[j])
                            # print("j",j)
                        indcies_of_items_to_append_to_skip_unique_list=[]
                        # print(items_of_alpha)
                        if i==len(new_states_only[index_of_current_item])-1:
                            # print("hellp")
                            for li in range(len(items_of_alpha)):
                                items_of_alpha[li]=self.remove_all_instances(items_of_alpha[li],-1)
                            actual_number_of_items_to_append=len(items_of_alpha)
                            for new_lists_index in range(len(items_of_alpha)):
                                
                                if sorted(list(set(items_of_alpha[new_lists_index]))) in new_states_only or sorted(list(set(items_of_alpha[new_lists_index]))) == []:
                                    actual_number_of_items_to_append-=1
                                    indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)
                
                            if actual_number_of_items_to_append==0  and no_of_lists_to_workon==0:
                                
                                new_states_flag=1
                            else:
                                for letter_index in range(len(dicotnray_of_current_item)):
                                    dicotnray_of_current_item[alpha[letter_index]]=sorted(list(set(items_of_alpha[letter_index])))
                                print("current sstate i will loop on now",new_states_only[index_of_current_item])
                                current_state_list="{"
                                for cc in range(len(new_states_only[index_of_current_item])):
                                    if cc==len(new_states_only[index_of_current_item])-1:
                                        current_state_list+=str(new_states_only[index_of_current_item][cc])
                                        current_state_list+="}"
                                    else:
                                        current_state_list+=str(new_states_only[index_of_current_item][cc])
                                        current_state_list+=','

                                # current_state_list=copy.deepcopy([str(cc) for cc in range(len(copy.deepcopy(new_states_only[index_of_current_item])))])
                                print("curent state list after looping",current_state_list)
                                # self.current_state_list.insert(0,'{')
                                # self.current_state_list.insert(len(current_state_transition),'}')
                                # print(new_states_only[index_of_current_item])

                                # current_state_list=",".join(copy.deepcopy(current_state_list))
                                self.dfa_table[current_state_list]=dicotnray_of_current_item
                                    # state_number_int=int(state_number_string)
                                # self.dfa_table['S'+state_number_string]=dicotnray_of_current_item
                                # state_number_string=int(state_number_string)+1
                                # state_number_string=str(state_number_string)
                                for new_lists in range(len(items_of_alpha)):
                                    if new_lists not in indcies_of_items_to_append_to_skip_unique_list:
                                        new_states_only.append(sorted(list(set(items_of_alpha[new_lists]))))
                                        no_of_lists_to_workon+=1

                    elif i>0:
                        index_of_current_letter_toappend=0
                        current_state_transition=self.get_epslin_closrue(new_states_only[index_of_current_item][i],nfa_table,alpha,breakpoint)
                        
                        for j in range(len(current_state_transition)):
                            items_of_alpha[index_of_current_letter_toappend].extend(current_state_transition[j])
                            index_of_current_letter_toappend+=1
                    
                        indcies_of_items_to_append_to_skip_unique_list=[]
                        if i==len(new_states_only[index_of_current_item])-1:
                            # print("hellp")
                            for li in range(len(items_of_alpha)):
                                items_of_alpha[li]=self.remove_all_instances(items_of_alpha[li],-1)
                            actual_number_of_items_to_append=len(items_of_alpha)
                            for new_lists_index in range(len(items_of_alpha)):
                                # print(items_of_alpha[new_lists_index])
                                if sorted(list(set(items_of_alpha[new_lists_index]))) in new_states_only or sorted(list(set(items_of_alpha[new_lists_index]))) == []:
                                    actual_number_of_items_to_append-=1
                                    indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)
                        
                            if actual_number_of_items_to_append==0 and no_of_lists_to_workon==0:
                                # print("hellp")
                                new_states_flag=1
                            else:
                                for letter_index in range(len(dicotnray_of_current_item)):
                                    dicotnray_of_current_item[alpha[letter_index]]=sorted(list(set(items_of_alpha[letter_index])))
                                    # state_number_int=int(state_number_string)
                                # print(new_states_only[index_of_current_item])
                                print("current sstate i will loop on now",new_states_only[index_of_current_item])
                                current_state_list="{"
                                for cc in range(len(new_states_only[index_of_current_item])):
                                    if cc==len(new_states_only[index_of_current_item])-1:
                                        current_state_list+=str(new_states_only[index_of_current_item][cc])
                                        current_state_list+="}"
                                    else:
                                        current_state_list+=str(new_states_only[index_of_current_item][cc])
                                        current_state_list+=','
                                # current_state_list=copy.deepcopy([str(cc) for cc in range(len(copy.deepcopy(new_states_only[index_of_current_item])))])

                                print("curent state list after looping",current_state_list)
                                # self.current_state_list.insert(0,'{')
                                # self.current_state_list.insert(len(current_state_transition),'}')
                                # current_state_list=",".join(current_state_list)
                                self.dfa_table[current_state_list]=dicotnray_of_current_item
                                # state_number_string=int(state_number_string)+1
                                # state_number_string=str(state_number_string)
                                for new_lists in range(len(items_of_alpha)):
                                    # print(items_of_alpha[new_lists])
                                    if new_lists not in indcies_of_items_to_append_to_skip_unique_list:
                                        new_states_only.append(sorted(list(set(items_of_alpha[new_lists]))))
                                        no_of_lists_to_workon+=1
                                        # counter+=1
                       
                index_of_current_item+=1
                no_of_lists_to_workon-=1


        # print(dfa_table)
        # print(new_states_only)
        return self.dfa_table


#######################################
print("=====================================================================================================================")

print("\t\t\t=================WELCOME AT NFA TO DFA MASTER=====================")
# print()
print("=====================================================================================================================")
print("DO YOU ALREADY HAVE A TABLE OR WOULD YOU LIKE TO PASS ONE MANUALLY ? (yes i have a table/no i want to input the table manually )")
choice=input("enter your choice")

if choice=="yes i have a table":
    x=dfa_nfa(table,alpha)
    print(x.show_nfa_repsenration_(table,alpha,len(alpha)))
    # print(x.convert_to_dfa(table,alpha,len(alpha)))
elif choice== "no i want to input the table manually":
    x=dfa_nfa()
    y=x.genreate_nfa()
    z=x.convert_to_dfa(y,x.alpha,len(x.alpha))
    print(z)


print("\t\t\t====================================\n====================================\n====================================\n====================================")
############################################
# x=['1','2','3']
# # y=str(x)
# print(x)
# print(type(x[0]))
















       
    # def generate_dfa(self):

                # self.dicotnray_of_current_item
                
                            # self.dicotnray_of_current_item


        # return self.table


# x=[[] for i in range(3)]
# print(x)


# x=dfa_nfa()

# y=x.genreate_nfa()
# print("nfa table:\n",x.table)
# print("\n\n\n\n")
# print("dfa table:\n",x.dfa_table)
# print("\n\n\n\n")

