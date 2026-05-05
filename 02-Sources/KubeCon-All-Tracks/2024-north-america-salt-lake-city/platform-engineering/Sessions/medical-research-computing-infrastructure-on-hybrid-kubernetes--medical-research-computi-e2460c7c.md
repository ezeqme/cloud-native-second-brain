---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Jennings Zhang", "Boston Children's Hospital"]
sched_url: https://kccncna2024.sched.com/event/1i7q6/medical-research-computing-infrastructure-on-hybrid-kubernetes-jennings-zhang-boston-childrens-hospital
youtube_search_url: https://www.youtube.com/results?search_query=Medical+Research+Computing+Infrastructure+on+Hybrid+Kubernetes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Medical Research Computing Infrastructure on Hybrid Kubernetes - Jennings Zhang, Boston Children's Hospital

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Jennings Zhang, Boston Children's Hospital
- Schedule: https://kccncna2024.sched.com/event/1i7q6/medical-research-computing-infrastructure-on-hybrid-kubernetes-jennings-zhang-boston-childrens-hospital
- Busca YouTube: https://www.youtube.com/results?search_query=Medical+Research+Computing+Infrastructure+on+Hybrid+Kubernetes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Medical Research Computing Infrastructure on Hybrid Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7q6/medical-research-computing-infrastructure-on-hybrid-kubernetes-jennings-zhang-boston-childrens-hospital
- YouTube search: https://www.youtube.com/results?search_query=Medical+Research+Computing+Infrastructure+on+Hybrid+Kubernetes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HclBYaLHHDw
- YouTube title: Medical Research Computing Infrastructure on Hybrid Kubernetes - Jennings Zhang
- Match score: 0.972
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/medical-research-computing-infrastructure-on-hybrid-kubernetes/HclBYaLHHDw.txt
- Transcript chars: 21752
- Keywords: cluster, software, research, hospital, question, compute, boston, children, analysis, actually, center, little, computing, course, technology, resources, architecture, public

### Resumo baseado na transcript

yeah thank you everyone for joining me here today uh we've had a bunch of talks about AI so let's try to get back on topic today uh I'm going to be talking about good old kubernetes and platform engineering so my name is Jennings I am a research scientist and software developer at the Boston Children's Hospital we are the world's largest pediatric research Enterprise and we received the most grant funding from the National Institutes of Health here in the US than any other institution we're also a

### Excerpt da transcript

yeah thank you everyone for joining me here today uh we've had a bunch of talks about AI so let's try to get back on topic today uh I'm going to be talking about good old kubernetes and platform engineering so my name is Jennings I am a research scientist and software developer at the Boston Children's Hospital we are the world's largest pediatric research Enterprise and we received the most grant funding from the National Institutes of Health here in the US than any other institution we're also a Harvard medical school affiliated teaching hospital within Children's I specifically work for an academic research lab known as the fnn DSC and our lab focuses on developing Advanced neural information processing systems you see neural information processing systems right you know made out of neurons the real ones you know axons and stuff I promise you AI will not be the big focus of this talk so at Children's we are researching experimental methods for doing in utero magnetic resonance imaging and what that means is we take MRIs of pregnant mothers and we look at their fetus's Anatomy imagine for a moment how difficult it is to tell a kid to sit still for the camera fetal MRI is kind of like that but even worse it's not exactly possible to tell a fetus to hold still for a moment although this is very very challenging we figured out ways to take repeated scans and Stitch together into one highquality image and we do this using machine learning of course we need a place to run all of these machine learning algorithms and today I'm going to be sharing the infrastructure we've developed to help facilitate this Advanced image analysis for clinical purposes it's by no surprise that we actually have this technology if you just do a simple very quick online search you can see that uh medical research machine learning has just blown up uh in fact the growth curve looks logistic it's maybe flattening out in the recent years but the point is we have a lot of this technology as we're doing more and more research we are acquiring new knowledge and that new knowledge leads to new research questions and more research of course but we have one remaining unsolved problem which is how can we take the products of research and actually deliver value in our case how can we improve patient care so it's no longer a question about whether or not we have the technology because the year is 2024 technology is awesome AI is awesome kubernetes is awesome but even though we have the technolo
