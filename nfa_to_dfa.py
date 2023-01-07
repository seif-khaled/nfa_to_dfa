import math
import collections
import copy 

############################
def get_epslin_closrue(element,nfa_table,alphates,br):
    stateS=[]
    index_of_alpha=0
    # print("current elemnt",nfa_table[element][alphates[index_of_alpha]])
    while index_of_alpha<br:
        # print("element",nfa_table[element])
        get_element=nfa_table[element][alphates[index_of_alpha]]
        # print(get_element)
        if get_element>=0:
            # print("my clousre is:",nfa_table[get_element]['ε'])
            # print("iam element",element,"and my value is ",get_element,"at",alpha[index_of_alpha]," and its closure is:",nfa_table[get_element]['ε'])
            # stateS.append(nfa_table[get_element]['ε'])
            stateS.append(copy.deepcopy(nfa_table[get_element]['ε'])) 
            index_of_alpha+=1
        elif get_element<0:
            # print("iam element",element,"and my value is ",get_element,"at",alpha[index_of_alpha]," and i dont have any closure")
            stateS.append([-1])
            index_of_alpha+=1
    return stateS
def remove_all_instances(LisT,item_to_remove):
    return [i for i in LisT if i!=item_to_remove]
##############################################
# table={0:{'a':-1,'ε':[0,1,3]},1:{'a':2,'ε':[1]},2:{'a':-1,'ε':[1,2,3]},3:{'a':-1,'ε':[3]}}
# table={0:{'a':1,'b':-1,'c':3, 'ε':[0]},1:{'a':-1,'b':2,'c':-1,'ε':[0,1]},2:{'a':1,'b':-1,'c':-1,'ε':[2]},3:{'a':-1,'b':-1,'c':2,'ε':[2,3]}}
table={0:{'0':1,'1':-1, 'ε':[0]},1:{'0':2,'1':4,'ε':[1]},2:{'0':-1,'1':3,'ε':[2]},3:{'0':-1,'1':-1,'ε':[0,3]},
4:{'0':5,'1':-1,'ε':[0,4]},5:{'0':-1,'1':-1,'ε':[0,5]}}

# table={0:{'a':1,'b':-1, 'ε':[0]},1:{'a':2,'b':4,'ε':[1]},2:{'a':-1,'b':3,'ε':[2]},3:{'a':-1,'b':-1,'ε':[0,3]},
# 4:{'a':5,'b':-1,'ε':[0,4]},5:{'a':-1,'b':-1,'ε':[0,5]}}

#########################################
# print("\n\n\n\n")
# elemnt_to_test=[0,3]
# alpha=['0','1']
# for i in range(len(elemnt_to_test)):
#     print(get_epslin_closrue(elemnt_to_test[i],table,alpha,len(alpha)))
############################################
alpha=['0','1']
# alpha=['a','b']
# alpha=['a','b','c']
# alpha=['a']
new_states_flag=0
dfa_table=dict()
breakpoint=len(alpha)
new_states_only=[copy.deepcopy(table[0]['ε'])]
no_of_lists_to_workon=1
index_of_current_item=0
state_number_string='0'
counter=0
# print(get_epslin_closrue(new_states_only[0][2],table,alpha,breakpoint))
while(new_states_flag!=1):
    # print("state working on:..",new_states_only[index_of_current_item])
    dicotnray_of_current_item=dict()
    # self.items_of_alpha=[ [] for i in range(len(self.alpha))]
    items_of_alpha=[]
    for i in range(len(alpha)):
        dicotnray_of_current_item[alpha[i]]=[]
    if index_of_current_item==len(new_states_only):
        new_states_flag=1
    else:
        for i in range(len(new_states_only[index_of_current_item])):
            # print(index_of_current_item)
            if i == 0:
                # print("current_state in ",new_states_only[0][i],"current letter",alpha[])
                current_state_transition=get_epslin_closrue(new_states_only[index_of_current_item][i],table,alpha,breakpoint)
                # print("current state iam wokring on",new_states_only[index_of_current_item],"my current transtions",current_state_transition)
                # print("current state iam at ",new_states_only[index_of_current_item],"my closure so far:",current_state_transition)

                # print(current_state_transition)
                # print("curent state transtions:",i,"=",current_state_transition)
                for j in range(len(current_state_transition)):
                    items_of_alpha.append(current_state_transition[j])
                    # print("j",j)
                indcies_of_items_to_append_to_skip_unique_list=[]
                # print(items_of_alpha)
                if i==len(new_states_only[index_of_current_item])-1:
                    # print("hellp")
                    for li in range(len(items_of_alpha)):
                        items_of_alpha[li]=remove_all_instances(items_of_alpha[li],-1)
                    actual_number_of_items_to_append=len(items_of_alpha)

                    # print(items_of_alpha)
                    for new_lists_index in range(len(items_of_alpha)):
                        print(items_of_alpha[new_lists_index])
                        if sorted(list(set(items_of_alpha[new_lists_index]))) in new_states_only or sorted(list(set(items_of_alpha[new_lists_index]))) == []:
                            actual_number_of_items_to_append-=1
                            indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)
                    # print("actual numebr of items to append",actual_number_of_items_to_append)
                    
                    # print(actual_number_of_items_to_append)
                    # print("current i",i,"incides to skip",indcies_of_items_to_append_to_skip_unique_list)

                    if actual_number_of_items_to_append==0  and no_of_lists_to_workon==0:
                        # print("hellp")
                        new_states_flag=1
                    else:
                        for letter_index in range(len(dicotnray_of_current_item)):
                            dicotnray_of_current_item[alpha[letter_index]]=sorted(list(set(items_of_alpha[letter_index])))
                            # state_number_int=int(state_number_string)
                        dfa_table['S'+state_number_string]=dicotnray_of_current_item
                        state_number_string=int(state_number_string)+1
                        state_number_string=str(state_number_string)
                        for new_lists in range(len(items_of_alpha)):
                            # print(items_of_alpha[new_lists])
                            if new_lists not in indcies_of_items_to_append_to_skip_unique_list:
                                new_states_only.append(sorted(list(set(items_of_alpha[new_lists]))))
                                no_of_lists_to_workon+=1

                # print(new_states_only)
                    # print(indcies_of_items_to_append_to_skip_unique_list)
            elif i>0:
                index_of_current_letter_toappend=0
                # print("curent state transtions:",i,"=",current_state_transition)
                current_state_transition=get_epslin_closrue(new_states_only[index_of_current_item][i],table,alpha,breakpoint)
                # print("current state iam wokring on",new_states_only[index_of_current_item],"my current transtions",current_state_transition)

                # print("current state iam at ",new_states_only[index_of_current_item],"my closure so far:",current_state_transition)
                for j in range(len(current_state_transition)):
                    items_of_alpha[index_of_current_letter_toappend].extend(current_state_transition[j])
                    index_of_current_letter_toappend+=1
                # print(items_of_alpha)
                # self.index_li_toremove
                
                #     if li<1:
                indcies_of_items_to_append_to_skip_unique_list=[]
                if i==len(new_states_only[index_of_current_item])-1:
                    # print("hellp")
                    for li in range(len(items_of_alpha)):
                        items_of_alpha[li]=remove_all_instances(items_of_alpha[li],-1)
                    actual_number_of_items_to_append=len(items_of_alpha)
                    for new_lists_index in range(len(items_of_alpha)):
                        # print(items_of_alpha[new_lists_index])
                        if sorted(list(set(items_of_alpha[new_lists_index]))) in new_states_only or sorted(list(set(items_of_alpha[new_lists_index]))) == []:
                            actual_number_of_items_to_append-=1
                            indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)
                    # print("current i",i,"incides to skip",indcies_of_items_to_append_to_skip_unique_list)
                    # print("actual numebr of items to append",actual_number_of_items_to_append)
                    # print(actual_number_of_items_to_append)
                    if actual_number_of_items_to_append==0 and no_of_lists_to_workon==0:
                        # print("hellp")
                        new_states_flag=1
                    else:
                        for letter_index in range(len(dicotnray_of_current_item)):
                            dicotnray_of_current_item[alpha[letter_index]]=sorted(list(set(items_of_alpha[letter_index])))
                            # state_number_int=int(state_number_string)
                        dfa_table['S'+state_number_string]=dicotnray_of_current_item
                        state_number_string=int(state_number_string)+1
                        state_number_string=str(state_number_string)
                        for new_lists in range(len(items_of_alpha)):
                            # print(items_of_alpha[new_lists])
                            if new_lists not in indcies_of_items_to_append_to_skip_unique_list:
                                new_states_only.append(sorted(list(set(items_of_alpha[new_lists]))))
                                no_of_lists_to_workon+=1
                                # counter+=1
                        # print(items_of_alpha)
                    # print(indcies_of_items_to_append_to_skip_unique_list)
        # print("loop number:",index_of_current_item,"items:",items_of_alpha,"current states found",new_states_only)

        # print("iam currnetly at state",new_states_only[index_of_current_item],"and my items are",items_of_alpha)
        # print(new_states_only[index_of_current_item],"items---->",items_of_alpha)
        index_of_current_item+=1
        no_of_lists_to_workon-=1
        # print("indcies current to skip: ",indcies_of_items_to_append_to_skip_unique_list)
    # print(new_states_only)

print(dfa_table)

###################################################

#####################
class dfa_nfa:
    def __init__(self):
        self.table=dict()
        self.dfa_table=dict()
    def remove_all_instances(self,LisT,item_to_remove):
        return [i for i in LisT if i!=item_to_remove]
    def get_epslin_closrue(self,element,nfa_table,alphates,breakpoint):
        self.stateS=[]
        self.index_of_alpha=0
        while self.index_of_alpha<breakpoint:
            self.get_element=nfa_table[element][alphates[self.index_of_alpha]]
            if self.get_element>=0:
                self.stateS.append(nfa_table[self.get_element]['ε'])
                self.index_of_alpha+=1
            elif self.get_element<0:
                self.stateS.append([-1])
                self.index_of_alpha+=1
        return self.stateS
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



        self.new_states_only=[self.table[0]['ε']]            
        self.new_states_flag=0
        self.index_of_current_item=0
        self.state_number_string='0'
        while(self.new_states_flag!=1):
            self.dicotnray_of_current_item=dict()
            # self.items_of_alpha=[ [] for i in range(len(self.alpha))]
            self.items_of_alpha=[]
            for i in range(len(self.alpha)):
                self.dicotnray_of_current_item[self.alpha[i]]=[]
            for i in range(len(self.new_states_only[self.index_of_current_item])):
                if i == 0:
                    self.current_state_transition=self.get_epslin_closrue(self.new_states_only[self.index_of_current_item][i],self.table,self.alpha,self.breakpoint)
                    for j in range(len(self.current_state_transition)):
                        self.items_of_alpha.append(self.current_state_transition[j])
                    

                elif i>0:
                    self.index_of_current_letter_toappend=0
                    self.current_state_transition=self.get_epslin_closrue(self.new_states_only[self.index_of_current_item][i],self.table,self.alpha,self.breakpoint)
                    for j in range(len(self.current_state_transition)):
                        self.items_of_alpha[self.index_of_current_letter_toappend].extend(self.current_state_transition[j])
                        self.index_of_current_letter_toappend+=1
                    # self.index_li_toremove
                    
                    #     if li<1:
                    self.indcies_of_items_to_append_to_skip_unique_list=[]
                    if i==len(self.new_states_only[self.index_of_current_item])-1:
                        for li in range(len(self.items_of_alpha)):
                            self.items_of_alpha[li]=self.remove_all_instances(self.items_of_alpha[li],-1)
                        self.actual_number_of_items_to_append=len(self.items_of_alpha)
                        for new_lists_index in range(len(self.items_of_alpha)):
                            if sorted(list(set(self.items_of_alpha[new_lists_index]))) in self.new_states_only:
                                self.actual_number_of_items_to_append-=1
                                self.indcies_of_items_to_append_to_skip_unique_list.append(new_lists_index)

                        if self.actual_number_of_items_to_append==0:
                            self.new_states_flag=1
                        else:
                            for letter_index in range(len(self.dicotnray_of_current_item)):
                                self.dicotnray_of_current_item[self.alpha[letter_index]]=sorted(list(set(self.items_of_alpha[letter_index])))
                                # state_number_int=int(state_number_string)
                            self.dfa_table['S'+self.state_number_string]=self.dicotnray_of_current_item
                            self.state_number_string=int(self.state_number_string)+1
                            self.state_number_string=str(self.state_number_string)
                            for new_lists in range(len(self.items_of_alpha)):
                                if new_lists not in self.indcies_of_items_to_append_to_skip_unique_list:
                                    self.new_states_only.append(self.items_of_alpha)
            self.index_of_current_item+=1
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

