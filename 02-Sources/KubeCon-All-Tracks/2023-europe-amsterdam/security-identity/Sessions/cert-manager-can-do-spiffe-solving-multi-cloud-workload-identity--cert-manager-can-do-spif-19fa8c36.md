---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security"]
speakers: ["Thomas Meadows", "Jetstack", "Joshua Van Leeuwen", "Diagrid"]
sched_url: https://kccnceu2023.sched.com/event/1HyVN/cert-manager-can-do-spiffe-solving-multi-cloud-workload-identity-using-a-de-facto-standard-tool-thomas-meadows-jetstack-joshua-van-leeuwen-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Cert-Manager+Can+Do+SPIFFE%3F+Solving+Multi-Cloud+Workload+Identity+Using+a+De+Facto+Standard+Tool+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Cert-Manager Can Do SPIFFE? Solving Multi-Cloud Workload Identity Using a De Facto Standard Tool - Thomas Meadows, Jetstack & Joshua Van Leeuwen, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Thomas Meadows, Jetstack, Joshua Van Leeuwen, Diagrid
- Schedule: https://kccnceu2023.sched.com/event/1HyVN/cert-manager-can-do-spiffe-solving-multi-cloud-workload-identity-using-a-de-facto-standard-tool-thomas-meadows-jetstack-joshua-van-leeuwen-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Cert-Manager+Can+Do+SPIFFE%3F+Solving+Multi-Cloud+Workload+Identity+Using+a+De+Facto+Standard+Tool+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Cert-Manager Can Do SPIFFE? Solving Multi-Cloud Workload Identity Using a De Facto Standard Tool.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1HyVN/cert-manager-can-do-spiffe-solving-multi-cloud-workload-identity-using-a-de-facto-standard-tool-thomas-meadows-jetstack-joshua-van-leeuwen-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Cert-Manager+Can+Do+SPIFFE%3F+Solving+Multi-Cloud+Workload+Identity+Using+a+De+Facto+Standard+Tool+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z7WSo-K0xuA
- YouTube title: Cert-Manager Can Do SPIFFE? Solving Multi-Cloud Workload... - Thomas Meadows & Joshua Leeuwen
- Match score: 0.736
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/cert-manager-can-do-spiffe-solving-multi-cloud-workload-identity-using/Z7WSo-K0xuA.txt
- Transcript chars: 36663
- Keywords: spiffy, manager, identity, driver, course, cluster, google, running, certificate, workload, actually, account, policy, called, another, hopefully, certificates, server

### Resumo baseado na transcript

hello everyone um thank you for coming to our talk I guess uh my name's Tom I'm a Solutions engineer at jetstack um I've been working with kubernetes now which is kind of scary I guess like three or four years yeah three years or so um I promise I don't still don't claim to be an expert but I work for a consultancy called jetstack um so we at least try and help people doing kubernetes um fail a lot along the way but you know that's all part

### Excerpt da transcript

hello everyone um thank you for coming to our talk I guess uh my name's Tom I'm a Solutions engineer at jetstack um I've been working with kubernetes now which is kind of scary I guess like three or four years yeah three years or so um I promise I don't still don't claim to be an expert but I work for a consultancy called jetstack um so we at least try and help people doing kubernetes um fail a lot along the way but you know that's all part of the process I'm joined here by my colleague Josh um yeah hi everyone I'm Josh um I'm a software engineer diagram so I'm a project maintainer for site manager I've been working on that project for quite a number of years and uh yeah more recently working a lot on dapper but yeah today we're going to talk about seven manager yeah um so I hope you're all here to hear the answer of the question cert manager can it do spiffy um so without further Ado let's try and answer that question do you want to do the slides because if I go to voice that then I've got the problem so I am a cert manager user please put your hands up if you've used cert manager yeah there we go see it's one of those tools where you know that like you're going to get a good response anyone that's heard of cert manager and wants to know a little bit more about it if the answer is yeah if the answer is yes we've got a booth I believe it's at K9 like the dog easy to remember um some of my colleagues at jetsack are here as well and they can help you along your way so I'm a term manager user and my journey with cert manager started about three or four years ago I was in my office um in in my my cubicle at VMware um it was a dark dreary evening and I spent many hours trying to get my GK cluster to expose my sock shop service to the public internet so I could show my parents even though they have absolutely no interest but there we go sorry mum and dad um I came up with this message and of course like if you want to look professional to all your friends and family this isn't exactly what you want off the face of it as I was still learning I didn't know why but it was something to do with the certificate apparently I needed a certificate to get this message to go away what an absolute bother so as any good engineer does I went back to Google and I asked Google how do I solve this problem on gke if you're on gke there's this tool called Google managed SSL which directly integrates into kubernetes on gke and has some custom crds to help you um vend and mint certi
