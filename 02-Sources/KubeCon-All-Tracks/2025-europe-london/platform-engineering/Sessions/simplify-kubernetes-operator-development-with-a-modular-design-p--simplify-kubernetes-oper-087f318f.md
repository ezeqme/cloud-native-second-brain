---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Mostafa Hadadian", "Alexander Lazovik", "University of Groningen"]
sched_url: https://kccnceu2025.sched.com/event/1txGB/simplify-kubernetes-operator-development-with-a-modular-design-pattern-mostafa-hadadian-alexander-lazovik-university-of-groningen
youtube_search_url: https://www.youtube.com/results?search_query=Simplify+Kubernetes+Operator+Development+With+a+Modular+Design+Pattern+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Simplify Kubernetes Operator Development With a Modular Design Pattern - Mostafa Hadadian & Alexander Lazovik, University of Groningen

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Mostafa Hadadian, Alexander Lazovik, University of Groningen
- Schedule: https://kccnceu2025.sched.com/event/1txGB/simplify-kubernetes-operator-development-with-a-modular-design-pattern-mostafa-hadadian-alexander-lazovik-university-of-groningen
- Busca YouTube: https://www.youtube.com/results?search_query=Simplify+Kubernetes+Operator+Development+With+a+Modular+Design+Pattern+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Simplify Kubernetes Operator Development With a Modular Design Pattern.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGB/simplify-kubernetes-operator-development-with-a-modular-design-pattern-mostafa-hadadian-alexander-lazovik-university-of-groningen
- YouTube search: https://www.youtube.com/results?search_query=Simplify+Kubernetes+Operator+Development+With+a+Modular+Design+Pattern+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m8ZnlZTo1OE
- YouTube title: Simplify Kubernetes Operator Development With a Modular Desi... Mostafa Hadadian & Alexander Lazovik
- Match score: 0.868
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/simplify-kubernetes-operator-development-with-a-modular-design-pattern/m8ZnlZTo1OE.txt
- Transcript chars: 14642
- Keywords: controller, operators, resource, values, operator, resources, controllers, platform, template, cluster, microcontrollers, templates, medium, custom, stateless, define, design, complex

### Resumo baseado na transcript

Uh today I'm going to take you on a journey that uh we took to build our AI serving platform using operators, the challenges we faced and how we overcome those with a design pattern. So if you also love Kubernetes, I guess we all love operators and let's see what and if you don't uh perhaps uh you will love it after this session. So based on this hype you will start building your operator on top of the tutorial what you learned and congratulation now you have your first operator and you're so happy with that. So controller reconciles the cluster and in doing that it means that it needs to translate your custom resource to built-in resources or let's say other resources which in turn and finally will be uh a built-in resource that Kubernetes knows and operates with that. So when there is such tool there let's use that in our benefit and put it in our uh design. So they don't care if you want to uh deploy it whatever way and translate it to whatever way in Kubernetes.

### Excerpt da transcript

Welcome. Uh today I'm going to take you on a journey that uh we took to build our AI serving platform using operators, the challenges we faced and how we overcome those with a design pattern. So yeah, I love Kubernetes and I guess you also do. So if you also love Kubernetes, I guess we all love operators and let's see what and if you don't uh perhaps uh you will love it after this session. So what's operator in a nutshell? operator extends a Kubernetes core API and in let's say in more descriptive way and by Kubernetes documentation operators are software extension to Kubernetes that make use of custom resource to make applications and their components. Uh operators follow Kubernetes principle notably the control loop. So essentially control loop are the execution logic and resources are the data and operators here are the autopilot of your cluster. That's cool right? So how uh the how controllers and uh um resources are doing that. So controllers are checking uh Kubernetes cluster and your desired uh state from your resource and reconcile these two.

So that's uh simply put. So now that we know what's operator, what is controller, what is resource, how should we start to build our operators. So how it started? Uh so you go search for a framework and you will perhaps go to the Google saying okay best framework for developing Kubernetes operators and you will probably hit operator SDK at least that's uh what I what I did and you will go to start uh with a tutorial how to build your first operators and what's better than the uh original website how can I build one you will start uh following the quick starts how to build your operators and you will perhaps build your first uh mimcache uh operator by following the tutorials and you're happy. So based on this hype you will start building your operator on top of the tutorial what you learned and congratulation now you have your first operator and you're so happy with that. But this was me uh two years ago. how it's going after that the uh controller logic get complex very quickly it's not uh it will be so many things that you never anticipated the first day and the CRDs are are like the a stone and when you want to change something in that it's like carving in a stone and it's in it's out there it's a central API you cannot change it easily and above all for the platform engineers it's the headache that only the creators may touch the operator code after two years and everybody will come to you saying okay I wa
