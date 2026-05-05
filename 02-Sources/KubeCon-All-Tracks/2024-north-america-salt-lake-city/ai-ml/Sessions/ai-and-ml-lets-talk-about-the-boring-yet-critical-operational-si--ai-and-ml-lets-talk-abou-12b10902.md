---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Rob Koch", "Slalom Build", "Milad Vafaeifard", "Epam"]
sched_url: https://kccncna2024.sched.com/event/1i7l4/ai-and-ml-lets-talk-about-the-boring-yet-critical-operational-side-rob-koch-slalom-build-milad-vafaeifard-epam
youtube_search_url: https://www.youtube.com/results?search_query=AI+and+ML%3A+Let%E2%80%99s+Talk+About+the+Boring+%28yet+Critical%21%29+Operational+Side+CNCF+KubeCon+2024
slides: []
status: parsed
---

# AI and ML: Let’s Talk About the Boring (yet Critical!) Operational Side - Rob Koch, Slalom Build & Milad Vafaeifard, Epam

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Rob Koch, Slalom Build, Milad Vafaeifard, Epam
- Schedule: https://kccncna2024.sched.com/event/1i7l4/ai-and-ml-lets-talk-about-the-boring-yet-critical-operational-side-rob-koch-slalom-build-milad-vafaeifard-epam
- Busca YouTube: https://www.youtube.com/results?search_query=AI+and+ML%3A+Let%E2%80%99s+Talk+About+the+Boring+%28yet+Critical%21%29+Operational+Side+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre AI and ML: Let’s Talk About the Boring (yet Critical!) Operational Side.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7l4/ai-and-ml-lets-talk-about-the-boring-yet-critical-operational-side-rob-koch-slalom-build-milad-vafaeifard-epam
- YouTube search: https://www.youtube.com/results?search_query=AI+and+ML%3A+Let%E2%80%99s+Talk+About+the+Boring+%28yet+Critical%21%29+Operational+Side+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5eQ1Kte-9Qw
- YouTube title: AI and ML: Let’s Talk About the Boring (yet Critical!) Operational Side- Rob Koch & Milad Vafaeifard
- Match score: 0.915
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/ai-and-ml-lets-talk-about-the-boring-yet-critical-operational-side/5eQ1Kte-9Qw.txt
- Transcript chars: 18872
- Keywords: hardware, clusters, resources, models, training, mesh, linker, working, course, gpu, support, cluster, critical, operational, compute, meshes, workloads, handle

### Resumo baseado na transcript

hello everyone in the audience out there people here hello we are here to talk about Ai and M ml as you can see but you know it is boring but critical right to all of your Ops I'm de we are both deaf um we use sign language we've got two interpreters here in the front row The Voice is coming from them not up here so just so you know make sure everybody can hear okay by the way I'm Rob cotch I'm from Seattle Washington and I

### Excerpt da transcript

hello everyone in the audience out there people here hello we are here to talk about Ai and M ml as you can see but you know it is boring but critical right to all of your Ops I'm de we are both deaf um we use sign language we've got two interpreters here in the front row The Voice is coming from them not up here so just so you know make sure everybody can hear okay by the way I'm Rob cotch I'm from Seattle Washington and I work for slalom as a principal with the data and platform engineering teams great to be here hi my name is Milad vafa I'm a lead software engineer for epam and I'm based in Hungary and I flew all the way in here for about 20 hours to get here so I'm recovered I'm here I'm happy to be here and I'm thrilled to see all of you people here giving me energy and it's like the medicine of the spirit we're here getting energy from you we're very excited to have this talk oh and by the way we are competitors so not today we're part of a community today so we're here together today why the focus on Ops well Ai and Ma machine learning are very glamorous applications but behind the scenes they need strong infrastructure there are some critical aspects that we must consider including compute resources separation of data reliability and observability service mees to simplify these challenges allowing Engineers to focus on AI and ml Innovations Ai and M ml are Hot Topics but for models and training and data sets and they need to work effectively thus they require reliable operational infrastructure we'll explore how service manager message meshes can offload much of this burden and allow us to focus on the exciting Ai and ml part kubernetes um is comes into play because the M Ai and ml workloads require significant computational resources and special Hardware kubernetes is all about managing and orchestrating tasks right so it's a natural fit for managing AI training Etc kubernetes can orchestrate these tasks but needs to handle the challenge of processing huge data sets while ensuring isolation between users and models these are Monster jobs we're talking about massive compute requirements massive data sets and massive images we would need to use specialized Hardware like gpus now of course they're hard to come by and they're pricey and these days usually available through your favorite hypercloud providers hypercloud and major vendors are hogging all the chips from the market but they can't help it because it's the Demand right some steps to take ins
