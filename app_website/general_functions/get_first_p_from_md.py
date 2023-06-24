import markdown as md

def get_first_p_from_md(project):
    
    md_html = md.markdown(project.content)
    p_close_tag_index = md_html.find("</p>") + 4
    return md_html[:p_close_tag_index]