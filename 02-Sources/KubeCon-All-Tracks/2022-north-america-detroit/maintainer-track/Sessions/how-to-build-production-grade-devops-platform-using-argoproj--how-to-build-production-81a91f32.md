---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Platform Engineering", "GitOps Delivery", "Community Governance"]
speakers: ["Alexander Matyushentsev", "Akuity", "Leonardo Luz Almeida", "Intuit"]
sched_url: https://kccncna2022.sched.com/event/182ME/how-to-build-production-grade-devops-platform-using-argoproj-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
youtube_search_url: https://www.youtube.com/results?search_query=How+To+Build+Production+Grade+DevOps+Platform+Using+Argoproj+CNCF+KubeCon+2022
slides: []
status: parsed
---

# How To Build Production Grade DevOps Platform Using Argoproj - Alexander Matyushentsev, Akuity & Leonardo Luz Almeida, Intuit

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Platform Engineering]], [[GitOps Delivery]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Alexander Matyushentsev, Akuity, Leonardo Luz Almeida, Intuit
- Schedule: https://kccncna2022.sched.com/event/182ME/how-to-build-production-grade-devops-platform-using-argoproj-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
- Busca YouTube: https://www.youtube.com/results?search_query=How+To+Build+Production+Grade+DevOps+Platform+Using+Argoproj+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre How To Build Production Grade DevOps Platform Using Argoproj.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182ME/how-to-build-production-grade-devops-platform-using-argoproj-alexander-matyushentsev-akuity-leonardo-luz-almeida-intuit
- YouTube search: https://www.youtube.com/results?search_query=How+To+Build+Production+Grade+DevOps+Platform+Using+Argoproj+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ohPKiGhhHoI
- YouTube title: How To Build Production Grade DevOps Platform Usin... Alexander Matyushentsev & Leonardo Luz Almeida
- Match score: 0.803
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/how-to-build-production-grade-devops-platform-using-argoproj/ohPKiGhhHoI.txt
- Transcript chars: 28271
- Keywords: application, argo, manage, provide, cluster, create, configure, everything, configuration, production, source, define, already, called, projects, platform, basically, folder

### Resumo baseado na transcript

uh I can provide my desired state in a yaml file in case of kubernetes and then we can collaborate together uh and store those files in git and somehow provide this uh this desired state of my infrastructure to kubernetes the thing is kubernetes does not provide out of a box a way for extracting this uh this last state from git and that's exactly where hargo City comes into place right Argo City is has exactly this responsibility to to get the to interface with with your git

### Excerpt da transcript

uh I can provide my desired state in a yaml file in case of kubernetes and then we can collaborate together uh and store those files in git and somehow provide this uh this desired state of my infrastructure to kubernetes the thing is kubernetes does not provide out of a box a way for extracting this uh this last state from git and that's exactly where hargo City comes into place right Argo City is has exactly this responsibility to to get the to interface with with your git provider and it will provide it will present this uh this latest state of your infrastructure to kubernetes and kubernetes will kick off the the reconciliation Loop to to to bring up your desired State into the live State okay and let's say I convince you to go with Argo CD and what is the first decision you have to make uh which git repo to use right this is the first question you have to answer and we basically understand that our there are two two different approaches you can take here one is uh dumping everything in one single repo meaning you're going to be using the same repo where you have all your source code to to um to store your your manifest files your your infrastructure uh configurations or you can use an independent repo which is totally disconnected from your source code and to to to store this uh these configuration files right maybe intuitively you might go with the first option this is what I did when I first installed Lego City myself and let me show you what are the the pros and cons of this approach um so basically with a centralized repo one of the one of the one of the pros right is that things are uh placed in the same Ripple obviously right you can just open a folder and see what is the current configuration of your production environment this is really is in the same repo where you have all your source code which is great uh but what are the disadvantages with this approach um so we understand that the authorization model might be uh uh harder to to to to to define basically because most of the times uh the role of the the the the member of your team who has asked who has access to to commit and merge uh code in in your master Branch or your main branch is not the same it's the same role of the person who has uh the the permission to deploy and change things in production right so this is this is something that is usually a requirement and if you have everything in one single repo it's going to be harder for you to come up with some uh configuration authorizi
