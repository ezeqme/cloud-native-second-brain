---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Security + Identity + Policy"
themes: ["Security", "Networking", "Kubernetes Core"]
speakers: ["Jay Chen", "Aviv Sasson", "Palo Alto Networks"]
sched_url: https://kccncna2021.sched.com/event/lV4u/insights-into-unsecured-kubernetes-in-the-wild-jay-chen-aviv-sasson-palo-alto-networks
youtube_search_url: https://www.youtube.com/results?search_query=Insights+into+Unsecured+Kubernetes+in+the+Wild+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Insights into Unsecured Kubernetes in the Wild - Jay Chen & Aviv Sasson, Palo Alto Networks

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Jay Chen, Aviv Sasson, Palo Alto Networks
- Schedule: https://kccncna2021.sched.com/event/lV4u/insights-into-unsecured-kubernetes-in-the-wild-jay-chen-aviv-sasson-palo-alto-networks
- Busca YouTube: https://www.youtube.com/results?search_query=Insights+into+Unsecured+Kubernetes+in+the+Wild+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Insights into Unsecured Kubernetes in the Wild.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV4u/insights-into-unsecured-kubernetes-in-the-wild-jay-chen-aviv-sasson-palo-alto-networks
- YouTube search: https://www.youtube.com/results?search_query=Insights+into+Unsecured+Kubernetes+in+the+Wild+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VGv32or8nmU
- YouTube title: Insights into Unsecured Kubernetes in the Wild - Jay Chen & Aviv Sasson, Palo Alto Networks
- Match score: 0.777
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/insights-into-unsecured-kubernetes-in-the-wild/VGv32or8nmU.txt
- Transcript chars: 24042
- Keywords: cluster, server, misconfigured, attacks, docker, hildegard, research, internet, honeypot, control, misconfiguration, attack, default, access, demons, deployed, containers, malware

### Resumo baseado na transcript

[Music] hello everyone and welcome to our session about insights into unsecured kubernetes in the wild we are really excited to be here virtually and hope you'll enjoy and learn from this talk all right so let's go over the agenda for today uh first we'll talk about attacks against misconfigured docker we'll talk about the notorious misconfiguration in docker that allow uh executing uh commands on docker demons and then we will talk about the trends the growing trends trends of attacking those demons and after that we'll go

### Excerpt da transcript

[Music] hello everyone and welcome to our session about insights into unsecured kubernetes in the wild we are really excited to be here virtually and hope you'll enjoy and learn from this talk all right so let's go over the agenda for today uh first we'll talk about attacks against misconfigured docker we'll talk about the notorious misconfiguration in docker that allow uh executing uh commands on docker demons and then we will talk about the trends the growing trends trends of attacking those demons and after that we'll go over the research we did which is splitted into two parts the first one is that we thought how kubernetes can be misconfigured and then we actively can scans the internet for such misconfigured kubernetes clusters and the results are going to shock you at least they shocked me after that we'll go and talk about the honeypot we deployed so we deployed those honeypots in order to see how frequent and what the the impact of those attacks on in on misconfigured kubernetes components so basically those honeypots are the misconfigured kubernetes components and then we'll show you the results of the the honeypots and then we'll talk about hildegard which is a crypto jacking malware we found using one of our honeypots it's the first ever documented malware that is designed to attack cubelets and we show you how it takes over all of the cluster and right after it will talk about how to avoid such misconfigurations so that stuff like this won't happen to you all right so let's go over who we are so me and jay both are security researchers at palo alto networks under unit 42 which is the division for uh threat intelligence in palo alto networks uh our area of expertise is the cloud we're both really enthusiastic about the cloud and all of our researchers were about anything that involves the cloud that includes vulnerabilities malware uh campaign attack surfaces and everything that is security wise interesting and as you see by the pictures we are both proud pet owners i got my dog and jay got his cats hopefully someday we'll be friends so let's start and talk about insecure docker demons so basically uh docker demon listen on a unix socket for api request and only root can acquire this unix socket so docker count on that and that's why they don't have any authentication or authorization mechanism inside so anything anyone that acquired this socket can just run any commands on the docker demon but there are also another option to configure docker
