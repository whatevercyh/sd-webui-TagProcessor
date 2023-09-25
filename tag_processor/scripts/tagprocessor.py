import contextlib
import gradio as gr
#from modules import scripts
import modules.scripts as scripts
import os
import re

def tag_split(tagstring):
    seplist=[', ',',']
    tag_list=re.split('|'.join(seplist),tagstring)
    return tag_list
    pass

def tag_count(tagdir):
    from collections import Counter
    tags=[]
    tagfiles=os.listdir(tagdir)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            with open(os.path.join(tagdir,tagfile),'r') as f:
                newtags=f.readline()
                newtags=newtags.split(', ')
                tags.extend(newtags)
                pass
            pass
        pass
    tags_count=str(Counter(tags))
    tags_count=tags_count.replace(', ',',\n')
    return tags_count
    pass

def tag_delete(tagdir,tags_to_delete):#tag删除
    #tags_to_delete=tags_to_delete.split(', ')#逗号或逗号空格分割
    if(isinstance(tags_to_delete,list)):
        pass
    else:
        tags_to_delete=tag_split(tags_to_delete)
        pass
    tags_to_delete=set(tags_to_delete)
    tagfiles=os.listdir(tagdir)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            tags=0
            with open(os.path.join(tagdir,tagfile),'r') as f:
                tags=f.readline()
                pass
            #tags=tags.split(', ')
            tags=tag_split(tags)
            with open(os.path.join(tagdir,tagfile),'w') as f:
                tags=set(tags)
                tags=tags-tags_to_delete
                #newtags=sorted(set(tags),key=tags.index)
                newtags=list(tags)
                newtags=", ".join(newtags)
                f.write(newtags)
                pass
            pass
        pass
    return tag_count(tagdir)
    pass

def tag_preserve(tagdir,tags_to_preserve):#tag反向删除
    #tags_to_delete=tags_to_delete.split(', ')#逗号或逗号空格分割
    tags_to_preserve=tag_split(tags_to_preserve)
    tags_to_preserve=set(tags_to_preserve)
    tagfiles=os.listdir(tagdir)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            tags=0
            with open(os.path.join(tagdir,tagfile),'r') as f:
                tags=f.readline()
                pass
            #tags=tags.split(', ')
            tags=tag_split(tags)
            with open(os.path.join(tagdir,tagfile),'w') as f:
                tags=set(tags)
                tags=tags_to_preserve & tags
                #newtags=sorted(set(tags),key=tags.index)
                newtags=list(tags)
                newtags=", ".join(newtags)
                f.write(newtags)
                pass
            pass
        pass
    return tag_count(tagdir)
    '''
    # tagfiles=os.listdir()
    # for tagfile in tagfiles:
    #     if(tagfile.endswith('.txt')):
    #         tags=0
    #         with open(tagfile,'r') as f:
    #             tags=f.readline()
    #             pass
    #         tags=tags.split(', ')
    #         newtags=[]
    #         for t in tags:
    #             if(t in tags_expected):
    #                 newtags.append(t)
    #                 pass
    #             pass
    #         with open(tagfile,'w') as f:
    #             newtags=", ".join(newtags)
    #             f.write(newtags)
    #             pass
    #         pass
    #     pass
    '''
    pass

def tag_exchange(tagdir,tags_old=None,tag_new=None):#tag替换，tags_old的词替换为tag_new,可用于将近意tag化简
    tagfiles=os.listdir(tagdir)
    tags_old=tag_split(tags_old)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            with open(os.path.join(tagdir,tagfile),'r') as f:
                tags=f.readline()
                pass
            #tags=tags.split(', ')
            tags=tag_split(tags)
            for i in range(len(tags)):
                if(tags[i] in tags_old):
                    tags[i]=tag_new
                    pass
                pass
            with open(os.path.join(tagdir,tagfile),'w') as f:
                tags=', '.join(tags)
                f.write(tags)
                pass
            pass
        pass
    return tag_quchong(tagdir)
    pass

def tag_containexchange(tagdir,tag_old=None,tag_new=None):#tag包含替换，将包含tag_old的词替换为tag_new
    tagfiles=os.listdir(tagdir)
    #tags_old=tag_split(tags_old)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            with open(os.path.join(tagdir,tagfile),'r') as f:
                tags=f.readline()
                pass
            #tags=tags.split(', ')
            tags=tag_split(tags)
            for i in range(len(tags)):
                '''
                if(tags[i] in tags_old):
                    tags[i]=tag_new
                    pass
                '''
                if(tag_old in tags[i]):
                    tags[i]=tag_new
                    pass
                pass
            with open(os.path.join(tagdir,tagfile),'w') as f:
                tags=', '.join(tags)
                f.write(tags)
                pass
            pass
        pass
    return tag_quchong(tagdir)
    pass

def tag_insert(tagdir,tags_to_insert):#添加tag
    tagfiles=os.listdir(tagdir)
    '''
    if(isinstance(tags_to_insert,str)):
        tags_to_insert=tags_to_insert.split(', ')
        pass
    '''
    tags_to_insert=tag_split(tags_to_insert)

    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            with open(os.path.join(tagdir,tagfile),'r') as f:
                tags=f.readline()
                pass
            #tags=tags.split(', ')
            tags=tag_split(tags)
            tags=tags_to_insert+tags
            tags=sorted(set(tags),key=tags.index)
            '''
            # tags=set(tags)#qu chong
            # tags=list(tags)#
            #tags.insert(0,triggertag)
            '''
            with open(os.path.join(tagdir,tagfile),'w') as f:
                tags=', '.join(tags)
                f.write(tags)
                pass
            pass
        pass
    return tag_count(tagdir)
    #print('tag inserted')
    pass

def tag_delete_asnum(tagdir,num):
    num=int(num)
    from collections import Counter
    tags=[]
    tagfiles=os.listdir(tagdir)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            with open(os.path.join(tagdir,tagfile),'r') as f:
                newtags=f.readline()
                newtags=newtags.split(',')
                for i in range(len(newtags)):
                    newtags[i]=newtags[i].strip()
                    pass
                tags.extend(newtags)
                pass
            pass
        pass
    tags_count=Counter(tags)
    #print(tags_count)
    tags_lf_=[]
    for key in tags_count:
        if(tags_count[key]<num):
            tags_lf_.append(key)
            pass
        pass
    tag_delete(tagdir,tags_lf_)
    return tag_count(tagdir)
    pass

def tag_quchong(tagdir):
    tagfiles=os.listdir(tagdir)
    for tagfile in tagfiles:
        if(tagfile.endswith('.txt')):
            with open(os.path.join(tagdir,tagfile),'r') as f:
                tags=f.readline()
                pass
            #tags=tags.split(', ')
            tags=tag_split(tags)
            tags=set(tags)
            tags=list(tags)
            with open(os.path.join(tagdir,tagfile),'w') as f:
                tags=', '.join(tags)
                f.write(tags)
                pass
            pass
        pass
    return tag_count(tagdir)
    pass

class reminderPlugin(scripts.Script):
    def __init__(self) -> None:
        super().__init__()
 
    def title(self):
        return "test-project"
 
    def show(self,is_img2img):
        return scripts.AlwaysVisible
 
    def ui(self,is_img2img):
        with gr.Group():
            with gr.Accordion("tag处理",open=False):
                tag_dir_text=gr.Textbox(label="Tag路径")
                tag_count_button=gr.Button(value="Tag计数",variant='primary')
                tag_count_text=gr.Textbox(label="Tag计数")
                tag_delete_button=gr.Button(value="Tag删除",variant='primary')
                tag_delete_text=gr.Textbox(label="Tag删除")
                tag_preserve_button=gr.Button(value="Tag反向删除",variant='primary')
                tag_preserve_text=gr.Textbox(label="Tag反向删除")
                tag_exchange_button=gr.Button(value="Tag替换",variant='primary')
                tag_containexchange_buttion=gr.Button(value="Tag包含替换",variant='primary')
                tags_old_text=gr.Textbox(label="旧tags（正常替换可多个，包含替换只能单个）")
                tag_new_text=gr.Textbox(label="新tag（单个）")
                tag_insert_button=gr.Button(value="添加tag",variant='primary')
                tags_insert_text=gr.Textbox(label="添加tag(可多个)")
                tag_deleteasnum_button=gr.Button(value="删除低数量tag",variant='primary')
                tag_num=gr.Number(precision=0)
                tag_quchong_button=gr.Button(value="Tag去重",variant='primary')
        with contextlib.suppress(AttributeError):
            if is_img2img:
                #根据当前的Tab来设置点击后数据输出的组件
                tag_count_button.click(fn=tag_count,inputs=tag_dir_text,outputs=tag_count_text)
                tag_delete_button.click(fn=tag_delete,inputs=[tag_dir_text,tag_delete_text],outputs=tag_count_text)
                tag_preserve_button.click(fn=tag_preserve,inputs=[tag_dir_text,tag_preserve_text],outputs=tag_count_text)
                tag_exchange_button.click(fn=tag_exchange,inputs=[tag_dir_text,tags_old_text,tag_new_text],outputs=tag_count_text)
                tag_containexchange_buttion.click(fn=tag_containexchange,inputs=[tag_dir_text,tags_old_text,tag_new_text],outputs=tag_count_text)
                tag_insert_button.click(fn=tag_insert,inputs=[tag_dir_text,tags_insert_text],outputs=tag_count_text)
                tag_deleteasnum_button.click(fn=tag_delete_asnum,inputs=[tag_dir_text,tag_num],outputs=tag_count_text)
                tag_quchong_button.click(fn=tag_quchong,inputs=tag_dir_text,outputs=tag_count_text)
            else:
                tag_count_button.click(fn=tag_count,inputs=tag_dir_text,outputs=tag_count_text)
                tag_delete_button.click(fn=tag_delete,inputs=[tag_dir_text,tag_delete_text],outputs=tag_count_text)
                tag_preserve_button.click(fn=tag_preserve,inputs=[tag_dir_text,tag_preserve_text],outputs=tag_count_text)
                tag_exchange_button.click(fn=tag_exchange,inputs=[tag_dir_text,tags_old_text,tag_new_text],outputs=tag_count_text)
                tag_containexchange_buttion.click(fn=tag_containexchange,inputs=[tag_dir_text,tags_old_text,tag_new_text],outputs=tag_count_text)
                tag_insert_button.click(fn=tag_insert,inputs=[tag_dir_text,tags_insert_text],outputs=tag_count_text)
                tag_deleteasnum_button.click(fn=tag_delete_asnum,inputs=[tag_dir_text,tag_num],outputs=tag_count_text)
                tag_quchong_button.click(fn=tag_quchong,inputs=tag_dir_text,outputs=tag_count_text)
                #根据当前的Tab来设置点击后数据输出的组件
                pass
        return [tag_dir_text,tag_count_button,tag_count_text,tag_delete_button,tag_delete_text]
