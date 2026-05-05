---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Hillai Ben-Sasson", "Ronen Shustin", "Wiz"]
sched_url: https://kccncna2023.sched.com/event/1TNeo/the-attacker-perspective-insights-from-hacking-alibaba-clouds-managed-k8s-environments-hillai-ben-sasson-ronen-shustin-wiz
youtube_search_url: https://www.youtube.com/results?search_query=The+Attacker+Perspective+-+Insights+From+Hacking+Alibaba+Cloud%27s+Managed+K8s+Environments+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Attacker Perspective - Insights From Hacking Alibaba Cloud's Managed K8s Environments - Hillai Ben-Sasson & Ronen Shustin, Wiz

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Chicago
- Speakers: Hillai Ben-Sasson, Ronen Shustin, Wiz
- Schedule: https://kccncna2023.sched.com/event/1TNeo/the-attacker-perspective-insights-from-hacking-alibaba-clouds-managed-k8s-environments-hillai-ben-sasson-ronen-shustin-wiz
- Busca YouTube: https://www.youtube.com/results?search_query=The+Attacker+Perspective+-+Insights+From+Hacking+Alibaba+Cloud%27s+Managed+K8s+Environments+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Attacker Perspective - Insights From Hacking Alibaba Cloud's Managed K8s Environments.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1TNeo/the-attacker-perspective-insights-from-hacking-alibaba-clouds-managed-k8s-environments-hillai-ben-sasson-ronen-shustin-wiz
- YouTube search: https://www.youtube.com/results?search_query=The+Attacker+Perspective+-+Insights+From+Hacking+Alibaba+Cloud%27s+Managed+K8s+Environments+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=d81qnGKv4EE
- YouTube title: The Attacker Perspective - Insights From Hacking Alibaba Cloud... Hillai Ben-Sasson & Ronen Shustin
- Match score: 0.878
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-attacker-perspective-insights-from-hacking-alibaba-clouds-managed/d81qnGKv4EE.txt
- Transcript chars: 35059
- Keywords: container, basically, access, alibaba, security, docker, interesting, exactly, whenever, internal, database, permissions, attacker, environments, customers, environment, question, actually

### Resumo baseado na transcript

all right hello everyone uh thank you very much for having me uh and welcome to my talk uh it's called the attacker perspective insights from Hocking Alibaba clouds internal kubernetes environments uh and the story I'm going to tell you here today is kind of a unique uh story and the cubec con view because we're not going to tell a kubernetes story from the point of view of like a developer or devop person or any of these things but from the opposite point of view uh how takeaways first of all uh it's worth noting that whenever you introduce uh kubernetes uh kubernetes cluster kubernetes uh pods to a multi-tenant environment it sort of complicates your security model because it provides additional attack surface uh it provides uh the attacker with access to stuff like uh identity service Cal share resources network resources uh that are all that are always uh uh better for you know expanding your attack surface uh so it's not it doesn't mean that you should never introduce kubernetes to multi tent uh

### Excerpt da transcript

all right hello everyone uh thank you very much for having me uh and welcome to my talk uh it's called the attacker perspective insights from Hocking Alibaba clouds internal kubernetes environments uh and the story I'm going to tell you here today is kind of a unique uh story and the cubec con view because we're not going to tell a kubernetes story from the point of view of like a developer or devop person or any of these things but from the opposite point of view uh how me uh as a hacker uh is looking on kubernetes environments like real life kuber environments of Alibaba Cloud uh and trying to basically hack them break them uh and specifically uh how uh we were able to start from a database instance uh on Al Cloud that belonged to us contained uh our own data only uh from there we were able to gain control over the entire kubernetes cluster uh and gain access to all the other customers databases uh that use the same service on Alig cloud and not only that but also we were able to gain right access to alibaba's internal container Reg containing all their uh images for different cloud services as well uh poison their images with whatever you know malicious scope that we wanted to uh insert into there and have that code execute on all the other customers databases as well and on other cloud services onb Cloud too so how do we do it uh what sort of mistakes and bugs we able to uh exploit here to get this crazy level of privilege and most importantly how can you guys prevent yourself from doing the similar mistakes uh when building these sort of services uh let's Dive Right In uh before we do uh allow me to introduce myself uh my name is Elon I'm also here on behalf of my teammate ran chin he couldn't be here uh with us but he did a lot of the stuff that I'm going to talk about today uh I am my name is as I said my Twitter handle is very conveniently just at HEI uh so uh if you want to uh hit me up there I post uh cool research stuff from time to time you're also very welcome to uh slide into my DMs uh I am 24 years old uh based in Israel um very proud to be Jewish and very proud to be Israeli um especially during these tough times uh and I am a security researcher as part of the wiiz research team what we do is basically Cloud security lat research uh which uh translated means a lot of the time working with uh real life uh big and complex um kubernetes and Docker based environments uh in lots of different cloud services and Cloud providers such as alib Cloud
