---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "SRE Reliability", "Community Governance"]
speakers: ["Jack Francis", "Microsoft"]
sched_url: https://kccncna2024.sched.com/event/1howV/sig-autoscaling-projects-update-jack-francis-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=SIG+Autoscaling+Projects+Update+CNCF+KubeCon+2024
slides: []
status: parsed
---

# SIG Autoscaling Projects Update - Jack Francis, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Jack Francis, Microsoft
- Schedule: https://kccncna2024.sched.com/event/1howV/sig-autoscaling-projects-update-jack-francis-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=SIG+Autoscaling+Projects+Update+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre SIG Autoscaling Projects Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1howV/sig-autoscaling-projects-update-jack-francis-microsoft
- YouTube search: https://www.youtube.com/results?search_query=SIG+Autoscaling+Projects+Update+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3fr2J3G1s1U
- YouTube title: SIG Autoscaling Projects Update - Jack Francis, Microsoft
- Match score: 0.809
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/sig-autoscaling-projects-update/3fr2J3G1s1U.txt
- Transcript chars: 30634
- Keywords: carpenter, cluster, scaling, autoscaler, autoscaling, serving, metrics, examples, resource, working, question, workloads, imagine, landed, gpu, definitely, packed, projects

### Resumo baseado na transcript

this is the maintainer track talk for Sig autoscaling I'm very honored to be representing Sig autoscaling I'm Jack Francis uh I work at Microsoft as I go through a bunch of slides with a ton of information uh it might not be clear the re the real reason we're here is to um try to expose the community to potentially new members invite new contributions so if I fail to do that in the slide content please um know that that's the the purpose of these talks we want I can hear you yes okay uh I came in a little bit late so apologies if you already covered this uh is the multi-dimensional autoscaler intended to supersede the others or is it intended to use them on the back end or to be

### Excerpt da transcript

this is the maintainer track talk for Sig autoscaling I'm very honored to be representing Sig autoscaling I'm Jack Francis uh I work at Microsoft as I go through a bunch of slides with a ton of information uh it might not be clear the re the real reason we're here is to um try to expose the community to potentially new members invite new contributions so if I fail to do that in the slide content please um know that that's the the purpose of these talks we want to make the project um transparent expose what we're working on share that we've got lots of problems to solve in the future and we'd love to have your help okay that's me it's Superfluous to put a picture of myself on the screen because you can just look at me but um now you get to see my son Jerome as well this an example of horizontal biological autoscaling it's a good audience all right uh quick overview of what we're going to talk about I actually did this agenda first and then all the content later so it might not match up exactly but basically I'm going to introduce you to the Sig we're going to talk um at a high level uh and a visual level about autoscaling Concepts how they work um brief mention of uh Carpenter one year later so Carpenter joined seag scaling last year so it's been super great to have them in the community um some stuff about Dr uh sh quick show hands does anybody know what Dr is I know you do Patrick that's cheating anybody seen any good Dr talks oh there's lots of them cool um we'll go up go through project updates there's a lot of projects in seato scaling so that'll be kind of a quick um run through of things that have happened in the last six months maybe 12 months future work and um some specific examples of where you can help but uh just generally speaking you can definitely help all right so um introduction about Sig Auto scaling the the the charter of Sig AO scaling kind it cuts across two uh Dimensions one is clusters and one is workloads in clusters we have projects like cluster autoscaler and Carpenter and for workloads we have horizontal pod autoscaler or HPA vertical pod autoscaler or vpa a uh emerging uh proposal called multi-dimensional pod autoscaling which is the two previous things combined into one there is a prototype project called balancer that uh a scaler uh governs that would love some help it's sort of stalled so we can talk about that briefly and then Adam resizer which is uh if you've been in kubernetes for a long time you'll know that's been aroun
