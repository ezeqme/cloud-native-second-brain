---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Business Value"
themes: ["Kubernetes Core"]
speakers: ["Mario Fahlandt", "Tobias Schneck", "Kubermatic GmbH"]
sched_url: https://kccnceu2022.sched.com/event/ytuM/running-kubernetes-in-a-manufacturing-line-what-could-possibly-go-wrong-mario-fahlandt-tobias-schneck-kubermatic-gmbh
youtube_search_url: https://www.youtube.com/results?search_query=Running+Kubernetes+in+a+Manufacturing+Line+%E2%80%93+What+Could+Possibly+Go+Wrong%3F+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Running Kubernetes in a Manufacturing Line – What Could Possibly Go Wrong? - Mario Fahlandt & Tobias Schneck, Kubermatic GmbH

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Business Value]]
- Temas: [[Kubernetes Core]]
- País/cidade: Spain / Valencia
- Speakers: Mario Fahlandt, Tobias Schneck, Kubermatic GmbH
- Schedule: https://kccnceu2022.sched.com/event/ytuM/running-kubernetes-in-a-manufacturing-line-what-could-possibly-go-wrong-mario-fahlandt-tobias-schneck-kubermatic-gmbh
- Busca YouTube: https://www.youtube.com/results?search_query=Running+Kubernetes+in+a+Manufacturing+Line+%E2%80%93+What+Could+Possibly+Go+Wrong%3F+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Running Kubernetes in a Manufacturing Line – What Could Possibly Go Wrong?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytuM/running-kubernetes-in-a-manufacturing-line-what-could-possibly-go-wrong-mario-fahlandt-tobias-schneck-kubermatic-gmbh
- YouTube search: https://www.youtube.com/results?search_query=Running+Kubernetes+in+a+Manufacturing+Line+%E2%80%93+What+Could+Possibly+Go+Wrong%3F+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nE2RnhgUTHI
- YouTube title: Running Kubernetes in a Manufacturing Line – What Could Possibly... Mario Fahlandt & Tobias Schneck
- Match score: 0.902
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/running-kubernetes-in-a-manufacturing-line-what-could-possibly-go-wron/nE2RnhgUTHI.txt
- Transcript chars: 26552
- Keywords: center, manufacturing, basically, everything, cluster, centers, clusters, master, everyone, customer, infrastructure, started, inside, single, firewall, currently, network, running

### Resumo baseado na transcript

okay hi everyone last talk we finally made it so only us and then we go out and drink beer and enjoy the rest of the sun so welcome everyone uh nice that you're still here with us and we are now here to talk about running kubernetes and manufacturing what could possibly go wrong yeah exactly so what is this about we luckily won a project um to implement kubernetes platform at a chemical producing company so that was the challenge itself because if you think about if you

### Excerpt da transcript

okay hi everyone last talk we finally made it so only us and then we go out and drink beer and enjoy the rest of the sun so welcome everyone uh nice that you're still here with us and we are now here to talk about running kubernetes and manufacturing what could possibly go wrong yeah exactly so what is this about we luckily won a project um to implement kubernetes platform at a chemical producing company so that was the challenge itself because if you think about if you produce chemical goods something went wrong then potentially it is not so good for everyone so yeah but before we go in detail a few things about us so my name is tobias you can say toby i'm working for cuba medic since four years um now as a principal architect helped to adapt the customer side kubernetes in a scalable way and yeah i'm mario i'm also working for clippermatic i'm a professional service kubernetes consultant we basically help our customers to build up their chromatic solution inside of their data centers or in the infrastructure and as you can see we're both from bavaria that's why we were litterhosen of course and now to go deeper into everything we need to go back in history so yes sorry it's friday and history lessons are always bad and no one likes history lessons but when we go back into the end of the 18th century we had the first weaveries that started mass producing goods this was called industry 1.0 now i mean it's new but we go with it and then we have a involvement in the industry line so we had mass production uh in this at the start of the 20th century and we had computer automation in this 70s so there were the first manufacturing lines that used robots and also kind of out started automating things and now we reach the point where we call it industry 4.0 and we are now at the point where we have interactive systems we have microchips in all of the manufacturing lines down to the to the single device and everything in the manufacturing plant is also virtualized so when we look at industry 4.0 it's like every manufacturing plant that we have need to be self-sufficient but also interconnected to different other plans because we uh the the whole production line maybe spends over a lot of factory plans and we are currently into the process that we have like data analytics in every single step and uh also security and observability that might as our systems are still running and also we want to improve every single step of our manufacturing process so the problem he
