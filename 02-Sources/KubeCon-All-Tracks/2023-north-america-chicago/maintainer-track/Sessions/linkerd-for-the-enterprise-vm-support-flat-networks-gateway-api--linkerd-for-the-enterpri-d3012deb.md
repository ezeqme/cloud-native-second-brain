---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["William Morgan", "Buoyant"]
sched_url: https://kccncna2023.sched.com/event/1R2uG/linkerd-for-the-enterprise-vm-support-flat-networks-gateway-api-and-more-william-morgan-buoyant
youtube_search_url: https://www.youtube.com/results?search_query=Linkerd+for+the+Enterprise%3A+VM+Support%2C+Flat+Networks%2C+Gateway+API%2C+and+More+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Linkerd for the Enterprise: VM Support, Flat Networks, Gateway API, and More - William Morgan, Buoyant

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: William Morgan, Buoyant
- Schedule: https://kccncna2023.sched.com/event/1R2uG/linkerd-for-the-enterprise-vm-support-flat-networks-gateway-api-and-more-william-morgan-buoyant
- Busca YouTube: https://www.youtube.com/results?search_query=Linkerd+for+the+Enterprise%3A+VM+Support%2C+Flat+Networks%2C+Gateway+API%2C+and+More+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Linkerd for the Enterprise: VM Support, Flat Networks, Gateway API, and More.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2uG/linkerd-for-the-enterprise-vm-support-flat-networks-gateway-api-and-more-william-morgan-buoyant
- YouTube search: https://www.youtube.com/results?search_query=Linkerd+for+the+Enterprise%3A+VM+Support%2C+Flat+Networks%2C+Gateway+API%2C+and+More+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=gKh1nWtxGTQ
- YouTube title: Linkerd for the Enterprise: VM Support, Flat Networks, Gateway API, and More - William Morgan
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/linkerd-for-the-enterprise-vm-support-flat-networks-gateway-api-and-mo/gKh1nWtxGTQ.txt
- Transcript chars: 34822
- Keywords: linkerd, question, gateway, linker, actually, mesh, network, workload, application, cluster, security, traffic, identity, proxies, ebpf, little, called, basically

### Resumo baseado na transcript

if you don't know what this little uh creature is in the bottom right when when linardy graduated we had to uh pick a mascot you know because they have all those cute little animals for kubernetes and for go and all that and so we tried to pick we tried to think of like what was the least cute animal that we could pick and lobster was the one that we ended on and um it's actually a blue lobster which is very rare you know so if you linkerd doio which please everyone join we can get to 10,000 people there um uh we've got mailing lists if you want the formal announcements we do uh the cncf funds formal thirdparty uh security audits yeah I think we have a pretty friendly and welcoming um Community I do have two quick ads um and then we'll jump into questions uh buoyant itself runs these free engineer focused uh training things called service mesh Academy so if you are interested in learning more about linkerd uh myself and a sir yeah great question so the question was you know Linker the data plate in lease is written in Rust what has the experience been like you know what kind of advantages what's been bad the the right place to learn more about that is

### Excerpt da transcript

if you don't know what this little uh creature is in the bottom right when when linardy graduated we had to uh pick a mascot you know because they have all those cute little animals for kubernetes and for go and all that and so we tried to pick we tried to think of like what was the least cute animal that we could pick and lobster was the one that we ended on and um it's actually a blue lobster which is very rare you know so if you ever see one of those in the wild don't don't eat it and then we had to answer a bunch of questions about like is does this Lobster what what gender is the lobster and I did a lot of research and it gets complicated so I'm I'm going to leave that for for you all to research at home how to tell you know uh the gender of a lobster all right I changed the subtitle just now those of you who were in the audience saw me do this live I promise it being here does not make you a boring person despite this very boring title and the fact that I am boring I'm going to try and make this really exciting this this is our uh linkerd maintainer kind of project update that we get to do every cubec con so I really appreciate you uh coming out here and and listening to me and you know feel free to uh raise your hand if you have a question at any point I'd love to make it more interactive and and not just me moning but I may get lost in the in the beauty of what I'm saying so you know we'll see how it goes all right this uh was supposed to be delivered by Alex uh unfortunately Alex is filling in for another talk um so I'm going to be delivering this in herstead but Alex will be delivering a talk that probably will be much more interesting than this one called 5 years of cloud native rust that's today at 2:30 on level three I think you can if I did my QR code right you should be able to just scan that otherwise you can just type in 1 R2 qn one of the things I'm only going to mention very briefly in this talk but Alex is really going to go into is uh the investment in Rust that we've made so you know it's been as you can see 5 years uh and a lot of what makes linkerd great today comes from this very early decision and you know a lot of kind of the pain and suffering that came along with that to adopt rust and to and to adopt this very particular approach where you know every aspect of the of of linker's data plan is um you know is kind of informed by not just rust but around the asynchronous network ecosystem uh that's been built up in Rust so please
