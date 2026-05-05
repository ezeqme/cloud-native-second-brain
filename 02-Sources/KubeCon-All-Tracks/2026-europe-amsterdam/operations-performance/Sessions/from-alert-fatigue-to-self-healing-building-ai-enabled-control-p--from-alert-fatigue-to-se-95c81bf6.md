---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Nuno Guedes", "Millennium bcp", "Yury Tsarev", "Upbound"]
sched_url: https://kccnceu2026.sched.com/event/2CVzm/from-alert-fatigue-to-self-healing-building-ai-enabled-control-planes-in-banking-nuno-guedes-millennium-bcp-yury-tsarev-upbound
youtube_search_url: https://www.youtube.com/results?search_query=From+Alert+Fatigue+To+Self-Healing%3A+Building+AI-Enabled+Control+Planes+in+Banking+CNCF+KubeCon+2026
slides: []
status: parsed
---

# From Alert Fatigue To Self-Healing: Building AI-Enabled Control Planes in Banking - Nuno Guedes, Millennium bcp & Yury Tsarev, Upbound

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nuno Guedes, Millennium bcp, Yury Tsarev, Upbound
- Schedule: https://kccnceu2026.sched.com/event/2CVzm/from-alert-fatigue-to-self-healing-building-ai-enabled-control-planes-in-banking-nuno-guedes-millennium-bcp-yury-tsarev-upbound
- Busca YouTube: https://www.youtube.com/results?search_query=From+Alert+Fatigue+To+Self-Healing%3A+Building+AI-Enabled+Control+Planes+in+Banking+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre From Alert Fatigue To Self-Healing: Building AI-Enabled Control Planes in Banking.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzm/from-alert-fatigue-to-self-healing-building-ai-enabled-control-planes-in-banking-nuno-guedes-millennium-bcp-yury-tsarev-upbound
- YouTube search: https://www.youtube.com/results?search_query=From+Alert+Fatigue+To+Self-Healing%3A+Building+AI-Enabled+Control+Planes+in+Banking+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oGk8jVz3qZ4
- YouTube title: From Alert Fatigue To Self-Healing: Building AI-Enabled Control Planes... Nuno Guedes & Yury Tsarev
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/from-alert-fatigue-to-self-healing-building-ai-enabled-control-planes/oGk8jVz3qZ4.txt
- Transcript chars: 18673
- Keywords: operation, cost, control, operations, crossplane, annotation, running, enabled, everything, recommendation, pretty, someone, remediation, caches, reason, standard, prompt, analysis

### Resumo baseado na transcript

This is from alert fatigue to selfhealing building AI enabled control planes in banking. I'm head of public cloud at Millennium PCP which for those of you who do not know is a bank in Portugal. The challenge of doing it manually as you grow in the size of your platform, in the complexity, in the in the service count, uh in the amount of signals you have to process, it just doesn't really scale and and this is something we all know, right? So I have a demo script that will help me uh uh to run the consist consistent demo and like in the before stage uh we are we running crossplane in standard operation we observing that one of the cache is stuck and now uh instead of that uh with AI enabled operation watch operations that I just demonstrated we can uh investigate uh the annotations so uh this annotation is set by watch operation by actual operations that invoke by watch operation on the on the cache right so it's there is no magic if you look at the uh at the spec uh so it will be cache demo stack and I will pop it to yq two uh standard spec uh composed objects right and this is di diagnosis uh annotation so

### Excerpt da transcript

Welcome everyone. This is from alert fatigue to selfhealing building AI enabled control planes in banking. And the reason why it says banking is Hi, I'm Nunu. I'm head of public cloud at Millennium PCP which for those of you who do not know is a bank in Portugal. And with me Yuri. Hey everyone, I'm Yuri from Abound and we are creators of course plane project. Super excited to be here. Please kick us off. >> Thank you very much. So, first of all, some warnings. Sorry, this session may use AI. With that out of the way, it does use AI. The promise of us is you kind of know these boxes signals. Let's keep the reason signals decides reconcile. If you know crossplane or other universal control planes, you're kind of familiar with this pattern. Something happens, there's an event, there's a decision being made. For instance, drift reconciliation and something reconciles. Today we are putting another box in the middle which sometimes reasons and why following the story that hey we're a bank. We kind of have a lot of regulatory compliance things to take care of.

It's people's money on one side of the room and on the other side it's AI. Uh we do not want to hallucinate and we have things like specific regulations things like the digital operational resiliency act in EU. We have a lot of regulators keeping up with what we do. We have operational resiliency as honestly a board topic. It's there there's there's a lot of people involved there. We cannot harm customers. We cannot have regulatory exposure. This means auditability, controlled change, predictable remediation. So it's perfect fit for AI, right? The reason why we pursue the AI story still is well, you know the story, right? The challenge of doing it manually as you grow in the size of your platform, in the complexity, in the in the service count, uh in the amount of signals you have to process, it just doesn't really scale and and this is something we all know, right? It's not know something new. It's always a story about toil. And I'd rather have people focusing on important stuff instead of here's incident number three and number four and number five and no cleaning up cues instead of going ahead of the curve with the additional topic of what happened, what changed, who approved, what was the outcome.

All of this being tracked, being auditable, being shown to everyone, including the regulators. Some years ago, we could say we had an observability problem. We're not there now. Perhaps we even have, sorry,
