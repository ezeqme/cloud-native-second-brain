---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Kante Yin", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwy/project-lightning-talk-sailing-multi-host-inference-with-lws-kante-yin-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Sailing+Multi-Host+Inference+with+LWS+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Sailing Multi-Host Inference with LWS - Kante Yin, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Kante Yin, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwy/project-lightning-talk-sailing-multi-host-inference-with-lws-kante-yin-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Sailing+Multi-Host+Inference+with+LWS+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Sailing Multi-Host Inference with LWS.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwy/project-lightning-talk-sailing-multi-host-inference-with-lws-kante-yin-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Sailing+Multi-Host+Inference+with+LWS+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PJ8qgKEwDyM
- YouTube title: Project Lightning Talk: Sailing Multi-Host Inference with LWS - Kante Yin, Maintainer
- Match score: 0.931
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-sailing-multi-host-inference-with-lws/PJ8qgKEwDyM.txt
- Transcript chars: 4334
- Keywords: leader, little, several, update, basically, worker, loading, restart, influence, across, create, staple, support, obviously, software, source, details, deepseek

### Resumo baseado na transcript

We talk a bit about this project later and I'm also the farmer of Infi. Infi is an open source uh community focused on building AI infrastructure. So with this uh architecture we offer se several uh capacities like the first one is about super port as a unit. third is about the scale sub source so uh we can scale the uh super port as we scale the deployment they they they share the same experience and the next part next part next next one is about the loading update. So we needed to place the leader pro uh leader port and the work p uh under the like the same network topology so they can have better performance.

### Excerpt da transcript

Hi all, welcome to join my lighting talk. Uh my name is Kent. So obviously I'm from Chelsea. Okay, I was I was joking. So I'm a software software engineer from dark cloud. I'm also the mater of little work set. We talk a bit about this project later and I'm also the farmer of Infi. Infi is an open source uh community focused on building AI infrastructure. So before we deep dive into the uh details about the little work set let's take back to the days where we want to build such a project. So obviously uh the large language model is growing rapidly uh it's like the recently the uh deepseek 400 and 5 billion and the deepseek R1 v R1 v3 the model cannot fit into a single node. So we need a new handler to help us to orchestration the uh influence service across nodes. So that's why we want to build such a project. We call it a little work [Music] set. Uh so from the right uh I think the left left side of the uh page is the overview about how little work set works. So basically little work set uh built on top of the stable set.

Here we create a leader work set and it will create a leader staple set and we have four replicas here. So we will have four leader ps and each leader port will create a worker staple set and here we have four worker stable set and each has two replica. So basically with all these set all these configuration set we have a leader pod and the two worker pods they will work as a group. So we call a super pod and here uh in the diagram we have four super pod. So with this uh architecture we offer se several uh capacities like the first one is about super port as a unit. So all parts of the super port they will share the uh same life circle and the second part is about the due template. So uh under some cases so the leader may uh behave different from the uh worker for example the leader may behave like a proxy only so it requires CPU only uh but it doesn't require any GPU so we need the dual template the third is about the scale sub source so uh we can scale the uh super port as we scale the deployment they they they share the same experience and the next part next part next next one is about the loading update.

So again we uh we can uh loading update the super port just we do with the deployment and the staple set they can loading update as so the super port caning update as a unit and the next one is about aware placement. So basically the models are shed across nodes. They have communication. So we needed to place the leader pro uh lead
