import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
from os import path

# root window

#variables
size=13
font = "Times"
color='#856ff8'

root = tk.Tk()
root.iconbitmap('icon\logo.ico')
root['background']=color
root.title('Post')
root.geometry("350x700")
root.resizable(False, False)


# store variables
title = tk.StringVar()
description = tk.StringVar()
#content = tk.StringVar()
category = tk.StringVar()
tags = tk.StringVar()



def save_clicked():
    """ callback when the save button clicked
    """
    
    #get values
    """The function get on a text widget requires two values: a starting position and an ending position.
    """
    TITLE = title.get().replace(',', ';')
    DESC = description.get().replace(',', ';')
    CONT = content_entry.get('1.0', tk.END).replace('\n', ' ').replace('\r', '').strip(" ").replace(',', ';')
    CATE = category.get().replace(',', ';')
    TAG = tags.get().replace(',', ';')
    
    # Save the data to a database or file
    head = 'TITLE,DESCRIPTION,CONTENT,CATEGORY,TAGS\n'
    line = f"{TITLE},{DESC},{CONT},{CATE},{TAG}"
    print(line)
    if TITLE=='' or DESC=='' or CONT=='' or CATE=='' or TAG=='' :
        showinfo(
            title='Information',
            message='pleas compete all informations')

    else:
        if path.exists("post.csv") is False:
            with open("post.csv","w",encoding="utf-8") as file:
                file.writelines(head)
                file.writelines(line)
                
        else :
            with open("post.csv","a",encoding="utf-8") as file:
                file.writelines("\n")
                file.writelines(line)
        
        # Clear entry widgets
        title_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
        content_entry.delete(1.0,tk.END)
        category_combobox.delete(0, tk.END)
        tags_entry.delete(0, tk.END)
        
        showinfo(
            title='Information',
            message='the post has been saved'
        )


def space():
    """make space beetwen two blocks
    """
    space = tk.Label(post, text="\n")
    space.config(bg=color)
    space.pack(fill='x')

# Post in frame
post = tk.Frame(root)
post['background']=color
post.pack(fill='x', expand=True)

first_title = ttk.Label(post,text='POST',font=("Times", "24", "bold italic"))
first_title['background']=color
first_title.pack()


#Title
title_label = ttk.Label(post, text="Title:",font=(font,size))
title_label['background']=color
title_label.pack(fill='x')

title_entry = ttk.Entry(post, textvariable=title)
title_entry.pack()

space()

#Description
description_label = ttk.Label(post, text="Short Description:",font=(font, size))
description_label['background']=color
description_label.pack(fill='x', expand=True)

description_entry = ttk.Entry(post, textvariable=description)
description_entry.pack()

space()

#Content
content_label = ttk.Label(post, text="Content:",font=(font, size))
content_label['background']=color
content_label.pack(fill='x', expand=True)

#content_entry = ttk.Entry(post, textvariable=content)
content_entry = ScrolledText(post ,width = 40, height = 10)
content_entry.pack()

space()

#Category
category_label=ttk.Label(post,text='Category:',font=(font, size))
category_label['background']=color
category_label.pack(fill='x', expand=True)

categories=['Food','Travel','Music','Business','Art','Sports','Book','Political','Religion','Movies','News']
category_combobox = ttk.Combobox(post, values=categories, textvariable=category)
category_combobox.pack()

space()

#Tags
tags_label = ttk.Label(post, text="Tags:",font=(font, size))
tags_label['background']=color
tags_label.pack(fill='x', expand=True)

tags_entry = ttk.Entry(post, textvariable=tags)
tags_entry.pack()

space()

#Save button
save_button = ttk.Button(post, text="Save", command=save_clicked)
save_button.pack(fill='y',side="bottom")


root.mainloop()