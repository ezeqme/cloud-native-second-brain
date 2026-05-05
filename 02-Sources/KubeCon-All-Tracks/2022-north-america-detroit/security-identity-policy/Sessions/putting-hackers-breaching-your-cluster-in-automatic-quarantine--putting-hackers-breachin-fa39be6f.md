---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Security + Identity + Policy"
themes: ["Security", "Kubernetes Core"]
speakers: ["Ziv Nevo", "IBM"]
sched_url: https://kccncna2022.sched.com/event/182Gf/putting-hackers-breaching-your-cluster-in-automatic-quarantine-ziv-nevo-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Putting+Hackers+Breaching+Your+Cluster+In+Automatic+Quarantine+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Putting Hackers Breaching Your Cluster In Automatic Quarantine - Ziv Nevo, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Security + Identity + Policy]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Ziv Nevo, IBM
- Schedule: https://kccncna2022.sched.com/event/182Gf/putting-hackers-breaching-your-cluster-in-automatic-quarantine-ziv-nevo-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Putting+Hackers+Breaching+Your+Cluster+In+Automatic+Quarantine+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Putting Hackers Breaching Your Cluster In Automatic Quarantine.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Gf/putting-hackers-breaching-your-cluster-in-automatic-quarantine-ziv-nevo-ibm
- YouTube search: https://www.youtube.com/results?search_query=Putting+Hackers+Breaching+Your+Cluster+In+Automatic+Quarantine+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RF9X1XRJ5Ko
- YouTube title: Putting Hackers Breaching Your Cluster In Automatic Quarantine - Ziv Nevo, IBM
- Match score: 0.985
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/putting-hackers-breaching-your-cluster-in-automatic-quarantine/RF9X1XRJ5Ko.txt
- Transcript chars: 17305
- Keywords: network, policies, connectivity, connections, cluster, application, request, synthesis, control, actually, allowed, security, traffic, enough, basically, outside, required, workflow

### Resumo baseado na transcript

so I'm Dave I'm a senior research scientist in IBM research in Israel and this talk was proposed by my colleague shmulich voimovic who unfortunately couldn't be here today and the title of this talk is putting hackers breaching your cluster in automatic quarantine so you can see this is a talk about security and I was told that talks about security should start with scaring the audience that something frightening is going to happen sir here is a scary thing really it is I have some of these in

### Excerpt da transcript

so I'm Dave I'm a senior research scientist in IBM research in Israel and this talk was proposed by my colleague shmulich voimovic who unfortunately couldn't be here today and the title of this talk is putting hackers breaching your cluster in automatic quarantine so you can see this is a talk about security and I was told that talks about security should start with scaring the audience that something frightening is going to happen sir here is a scary thing really it is I have some of these in my backyard and they are nasty they are very quick and when they bite it really hurts so don't mess with these creatures um however I got used to them and now what really scares me is that too many Cloud applications do not apply now that's scary you don't seem scared enough so let me explain why this is so scary mainly because without a gas control your application is exposed to many many attacks and for example reverse shell attacks data leaks if you don't control what gets out of your cluster everything can get out can get out of your cluster and it is very likely that there are hackers that may already be in in your have control on on some microservices in your application so previously it was thought that if I protect my English good enough this is well this should be enough but there are Insider threats there always have been and we know that social engineering and spear phishing attacks are getting more and more sophisticated and this also allows hackers to get into your application and those of you who attended the security cone may have heard the very frightening number of 742 percent rise in supply chain attacks in the last three years so this is really scary so basically it's not a question of if it's a question of when your application will be hacked and you should be prepared and at least protect your egress so data doesn't get out so easily so this is the customary slide with some recent attacks that maybe it could be prevented with tighter egress control oh and there is also compliance so and these days you have standards so and the nist sc7 tells you that you should deny network communications traffic by default and allow natural Communications traffic by exception and manage interfaces and only those system connections which are essential and approved order and are allowed and you may say okay but I closed the interest side matte this doesn't mean that a micro service of yours cannot talk to the outside internet and so you must control also its igles
