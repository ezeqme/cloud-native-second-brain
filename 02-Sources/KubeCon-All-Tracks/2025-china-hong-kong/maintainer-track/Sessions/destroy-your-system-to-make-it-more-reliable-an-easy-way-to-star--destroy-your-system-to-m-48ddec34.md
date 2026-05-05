---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Sayan Mondal", "Harness"]
sched_url: https://kccncchn2025.sched.com/event/1x5hT/destroy-your-system-to-make-it-more-reliable-an-easy-way-to-start-chaos-engineering-with-litmuschao-sayan-mondal-harness
youtube_search_url: https://www.youtube.com/results?search_query=Destroy+Your+System+To+Make+It+More+Reliable%3A+An+Easy+Way+To+Start+Chaos+Engineering+With+LitmusChao+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Destroy Your System To Make It More Reliable: An Easy Way To Start Chaos Engineering With LitmusChao - Sayan Mondal, Harness

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: China / Hong Kong
- Speakers: Sayan Mondal, Harness
- Schedule: https://kccncchn2025.sched.com/event/1x5hT/destroy-your-system-to-make-it-more-reliable-an-easy-way-to-start-chaos-engineering-with-litmuschao-sayan-mondal-harness
- Busca YouTube: https://www.youtube.com/results?search_query=Destroy+Your+System+To+Make+It+More+Reliable%3A+An+Easy+Way+To+Start+Chaos+Engineering+With+LitmusChao+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Destroy Your System To Make It More Reliable: An Easy Way To Start Chaos Engineering With LitmusChao.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5hT/destroy-your-system-to-make-it-more-reliable-an-easy-way-to-start-chaos-engineering-with-litmuschao-sayan-mondal-harness
- YouTube search: https://www.youtube.com/results?search_query=Destroy+Your+System+To+Make+It+More+Reliable%3A+An+Easy+Way+To+Start+Chaos+Engineering+With+LitmusChao+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HRZ79SmUbv0
- YouTube title: Destroy Your System To Make It More Reliable: An Easy Way To Start Chaos Engineering... Sayan Mondal
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/destroy-your-system-to-make-it-more-reliable-an-easy-way-to-start-chao/HRZ79SmUbv0.txt
- Transcript chars: 23182
- Keywords: application, litmos, litmus, experiment, multiple, engineering, infrastructure, couple, product, support, execution, inject, course, control, runner, itself, faults, specific

### Resumo baseado na transcript

Hey guys, uh very good morning uh and hope this is the first actual maintainer track session after the keynote and um I hope I can give you an overview of chaos engineering um the product litmos chaos open source chaos engineering. So today's topic is going to be how we can destroy our production systems uh to test resilience in a safe way using one of the open source chaos engineering tooling. So everything is dependent on a lot more things these days with the complicated architectures. You can also do the top two but it's like a granular solution where you can test individual layers and also club them together uh into what we call the reliability proliferation challenge. Now sometimes the problem is with the application itself because a lot of the time there might be bad code unhandled edge cases and a lot of the time it's just uh unexpected system load that might happen due to some uh traffic injection. Uh now often times cloud providers and kubernetes um is not really 100% reliable because uh you could receive device failures like um hard drives crashing uh or power supplies failing or memory leak buildup and so on.

### Excerpt da transcript

Hey guys, uh very good morning uh and hope this is the first actual maintainer track session after the keynote and um I hope I can give you an overview of chaos engineering um the product litmos chaos open source chaos engineering. So today's topic is going to be how we can destroy our production systems uh to test resilience in a safe way using one of the open source chaos engineering tooling. My name is Shy. I'm a senior software engineer at harness. Uh and I am also a maintainer and community manager of uh product called MSIOS which is the CNCF incubating open source project. Uh I also actively participate in LFX mentorship for this product. Um and uh we also will be doing the term three as well. Um and lastly I've been practicing chaos engineering for the last uh three and three and a half four years. Uh and these are some of my social uh handles. So before we jump into chaos engineering, I would want to quickly talk about resilience uh why it's required. So there's cloud native systems everywhere these days with distributed systems and there's a lot of interdependent failures that occur because everything is connected.

So 80% of the cloud native infrastructure is connected and if one fails the other fails because of uh the cascading uh downtimes. Also we have a lot of complex architectures these days. You usually before we used to ship just one thing uh we had less release cycles now we have a lot more. So everything is dependent on a lot more things these days with the complicated architectures. So reliability is really crucial. Uh and a lot of the times you often time test the top of the layer which is the application layer itself. We never trickle down to the bottom. Rarely do we ever test the infrastructure or the underlying platform services or the cloud native services. We generally test our application and sometimes uh we also test the application dependencies but rarely do we even touch the infrastructure layer. So this is the application pyramid, the infrastructure pyramid as we call it. Um and chaos engineering specifically focuses on touching the bottom three layers. You can also do the top two but it's like a granular solution where you can test individual layers and also club them together uh into what we call the reliability proliferation challenge.

Now outages are expensive and chaos engineering is one of such practices that help prevent them. Now they do lead to a lot of uh financial losses and reputational damage as we know. Um and
