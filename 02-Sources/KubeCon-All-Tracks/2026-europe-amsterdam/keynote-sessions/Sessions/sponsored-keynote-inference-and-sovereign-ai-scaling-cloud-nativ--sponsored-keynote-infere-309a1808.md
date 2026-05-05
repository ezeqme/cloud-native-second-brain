---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Keynote Sessions"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Karena Angell", "Technical Strategist", "Global Engineering", "Red Hat", "Vincent Caldeira", "Chief Technology Officer", "APAC", "Red Hat"]
sched_url: https://kccnceu2026.sched.com/event/2HgH3/sponsored-keynote-inference-and-sovereign-ai-scaling-cloud-native-ai-with-control-and-compliance-karena-angell-technical-strategist-global-engineering-red-hat-vincent-caldeira-chief-technology-officer-apac-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Inference+and+Sovereign+AI%3A+Scaling+Cloud-Native+AI+with+Control+and+Compliance+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Sponsored Keynote: Inference and Sovereign AI: Scaling Cloud-Native AI with Control and Compliance - Karena Angell, Technical Strategist, Global Engineering, Red Hat & Vincent Caldeira, Chief Technology Officer, APAC, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Karena Angell, Technical Strategist, Global Engineering, Red Hat, Vincent Caldeira, Chief Technology Officer, APAC, Red Hat
- Schedule: https://kccnceu2026.sched.com/event/2HgH3/sponsored-keynote-inference-and-sovereign-ai-scaling-cloud-native-ai-with-control-and-compliance-karena-angell-technical-strategist-global-engineering-red-hat-vincent-caldeira-chief-technology-officer-apac-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Inference+and+Sovereign+AI%3A+Scaling+Cloud-Native+AI+with+Control+and+Compliance+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Sponsored Keynote: Inference and Sovereign AI: Scaling Cloud-Native AI with Control and Compliance.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2HgH3/sponsored-keynote-inference-and-sovereign-ai-scaling-cloud-native-ai-with-control-and-compliance-karena-angell-technical-strategist-global-engineering-red-hat-vincent-caldeira-chief-technology-officer-apac-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Sponsored+Keynote%3A+Inference+and+Sovereign+AI%3A+Scaling+Cloud-Native+AI+with+Control+and+Compliance+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jcpWtyetjcw
- YouTube title: Sponsored Keynote: Inference and Sovereign AI: Scaling Cloud-Native... K. Angell & V. Caldeira (ASL)
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/sponsored-keynote-inference-and-sovereign-ai-scaling-cloud-native-ai-w/jcpWtyetjcw.txt
- Transcript chars: 3525
- Keywords: inference, scaling, sovereign, routing, control, gateway, compliance, finally, massive, organizations, already, yesterday, sovereignty, traditional, models, memory, balancing, handle

### Resumo baseado na transcript

Generative AI is finally getting out of the labs into a production system. 79% of organizations already view sovereign AI as a top strategic priority. Crucially, this open approach allows you to handle regulatory compliance at scale, in particular mandates such as the EU AI Act. LLMD acts as the orchestrator, delivering highly cost-effective distributed inference through intelligent scheduling. To achieve this optimization, LLMD is fundamentally upgrading Kubernetes with AI-aware routing fabric. We're moving far beyond simple round robin scaling to multi-dimensional, state-aware scheduling that squeezes every ounce of performance out of your expensive GPUs.

### Excerpt da transcript

Good morning, KubeCon. Hey. We have reached a tipping point. Generative AI is finally getting out of the labs into a production system. But we now run into a massive roadblock. How do we scale up without surrendering control of our data? The industry has spoken. 79% of organizations already view sovereign AI as a top strategic priority. And we heard yesterday that 60% of organizations are already using Kubernetes to scale their AI workload. So, the challenge we have now is how do we bridge these two worlds? How do we bring the scale of Kubernetes to support our AI model and our data sovereignty requirements? Scaling GenAI is nothing like scaling web application. Traditional web apps are lightweight. They are predictable. AI models, they are heavy, they are memory hungry, and they need to serve really non-uniform workloads. Because of that, the traditional way of routing traffic and load balancing is broken for AI. The result, painful delays, massive hardware inefficiency, and cloud bills just jumping through the roof.

If we want to run GenAI at scale, we can't rely on yesterday's plumbing. We need a platform that is fully AI aware, built from the ground up to handle the sheer width of model and their complexity. So, we really need an open blueprint for AI that is cloud native. But first, let's clarify that true sovereignty doesn't mean isolation. It actually means interoperability and the ability to avoid vendor locking. To do this, we are building a Kubernetes native AI factory. By using an open-source foundation, we retain the technical and operational control over the entire stack. This modular blueprint has a huge advantage. It allows you to deploy your artificial intelligence anywhere, in your cloud, at the edge, into your sovereign cloud, as well. Crucially, this open approach allows you to handle regulatory compliance at scale, in particular mandates such as the EU AI Act. And to make this AI factory a reality, we have been the leading developers of the new open-source AI inference stack based on vLLM and LLMD.

And migrate and integrating it natively into Kubernetes. To serve models seamlessly, we first leverage KServe. It acts as our standard abstraction layer, providing production-ready auto scaling, and hiding the underlying complexity. Next, we use Kubernetes to scale dynamically. We are bringing enterprise-grade orchestration to AI with the new API inference gateway, or the gateway API inference extension, pardon me, uh to enable true AI-awar
