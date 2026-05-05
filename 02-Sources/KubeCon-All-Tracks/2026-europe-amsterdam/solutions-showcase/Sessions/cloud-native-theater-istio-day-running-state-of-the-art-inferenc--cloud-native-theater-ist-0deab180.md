---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["AI ML", "Networking"]
speakers: ["Jackie Maertens", "Microsoft and Nili Guy", "IBM"]
sched_url: https://kccnceu2026.sched.com/event/2EG0w/cloud-native-theater-istio-day-running-state-of-the-art-inference-with-istio-and-llm-d-jackie-maertens-microsoft-and-nili-guy-ibm
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Running+State+of+the+Art+Inference+with+Istio+and+LLM-D+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | Istio Day: Running State of the Art Inference with Istio and LLM-D - Jackie Maertens, Microsoft and Nili Guy, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[AI ML]], [[Networking]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jackie Maertens, Microsoft and Nili Guy, IBM
- Schedule: https://kccnceu2026.sched.com/event/2EG0w/cloud-native-theater-istio-day-running-state-of-the-art-inference-with-istio-and-llm-d-jackie-maertens-microsoft-and-nili-guy-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Running+State+of+the+Art+Inference+with+Istio+and+LLM-D+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | Istio Day: Running State of the Art Inference with Istio and LLM-D.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0w/cloud-native-theater-istio-day-running-state-of-the-art-inference-with-istio-and-llm-d-jackie-maertens-microsoft-and-nili-guy-ibm
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+Istio+Day%3A+Running+State+of+the+Art+Inference+with+Istio+and+LLM-D+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dr03NZmau5g
- YouTube title: Cloud Native Theater | Istio Day: Running State of the Art Inference... Jackie Maertens and Nili Guy
- Match score: 0.924
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-istio-day-running-state-of-the-art-inference-with/dr03NZmau5g.txt
- Transcript chars: 20496
- Keywords: inference, gateway, request, istio, server, endpoint, basically, requests, scheduler, actually, decode, routing, resource, picker, response, choose, controller, control

### Resumo baseado na transcript

And I'm Jackie, software engineer from Microsoft, Istio security maintainer and co-lead of our product security working group. So, today we'll be talking about running state-of-the-art inference with Istio and LMD. If we are trying to do regular round-robin load balancing with those requests, we'll get we will get very bad performance in aspect of the performance and the cost. So, the the the industry challenge of scaling difference has a few aspects. We need to do We need to understand how we are distributing the workload in accordance to the the request and the required SLO, so we'll get the the best performance. We have valid paths that explain how to configure the system based on the workload and how to utilize and how to do distributed inference at scale.

### Excerpt da transcript

So, hello everyone. I'm Nili. I'm from a IBM. And I'm Jackie, software engineer from Microsoft, Istio security maintainer and co-lead of our product security working group. So, today we'll be talking about running state-of-the-art inference with Istio and LMD. I'm from the from the LMD team. Yeah, please go ahead. So, why Istio needs to care about AI? I don't know if any of you were today at the keynote, but I think that to the people that were, you understand that AI workload is becoming the next major workload. And not only that, um when talking about AI workloads, there are inference and there is tuning. And what you can see that the inference is taking more and more bigger part, almost 70% of the AI workloads are inference. So, um what's the difference? Meaning we we had microservices and HTTP requests, and now we have AI workloads. Why do we need to do anything different? If we're looking at HTTP requests, first of all, the hardware is cheaper. Using CPU and GPU is something that makes a lot of difference.

We need to be more efficient, more cost-effective. HTTP requests are faster, are uniform, whereas LLM requests, inference requests, are slow. They're non-uniform. Some requests can have long prompts, long response, others can be faster. And as we said, this is like 6 to 9 more expensive requests. So, we need to do something different. If we are trying to do regular round-robin load balancing with those requests, we'll get we will get very bad performance in aspect of the performance and the cost. So, we need to adjust. So, the the the industry challenge of scaling difference has a few aspects. As we said, they are variable, resource-heavy. We need to ensure SLO. What is SLO? We have throughput, but we have a new notion of time to first token. Time to first token, it means you're you're talking with ChatGPT. You're sending a question. When will you get a response? Where will the model server start generating you the the first token? And there is latency. So, we need to optimize the utilization to to reduce this complexity.

The hardware is heterogeneous. Sometimes where the cluster has GPUs with that are more expensive, more expensive accelerators, cheaper. We need to do We need to understand how we are distributing the workload in accordance to the the request and the required SLO, so we'll get the the best performance. And KV cache management, we'll touch more on that and explain why KV cache is one of the major things that are important in infere
