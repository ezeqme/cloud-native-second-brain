---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["Observability", "Kubernetes Core"]
speakers: ["Srinivasan Parthasarathy", "IBM", "Shubham Chaudhary", "JFrog"]
sched_url: https://kccncna2022.sched.com/event/182FP/unified-chaos-injection-and-slo-validation-experiments-in-kubernetes-srinivasan-parthasarathy-ibm-shubham-chaudhary-jfrog
youtube_search_url: https://www.youtube.com/results?search_query=Unified+Chaos+Injection+And+SLO+Validation+Experiments+In+Kubernetes+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Unified Chaos Injection And SLO Validation Experiments In Kubernetes - Srinivasan Parthasarathy, IBM & Shubham Chaudhary, JFrog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Observability]], [[Kubernetes Core]]
- País/cidade: United States / Detroit
- Speakers: Srinivasan Parthasarathy, IBM, Shubham Chaudhary, JFrog
- Schedule: https://kccncna2022.sched.com/event/182FP/unified-chaos-injection-and-slo-validation-experiments-in-kubernetes-srinivasan-parthasarathy-ibm-shubham-chaudhary-jfrog
- Busca YouTube: https://www.youtube.com/results?search_query=Unified+Chaos+Injection+And+SLO+Validation+Experiments+In+Kubernetes+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Unified Chaos Injection And SLO Validation Experiments In Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182FP/unified-chaos-injection-and-slo-validation-experiments-in-kubernetes-srinivasan-parthasarathy-ibm-shubham-chaudhary-jfrog
- YouTube search: https://www.youtube.com/results?search_query=Unified+Chaos+Injection+And+SLO+Validation+Experiments+In+Kubernetes+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=aeTCYm1x-co
- YouTube title: Unified Chaos Injection And SLO Validation... - Srinivasan Parthasarathy & Shubham Chaudhary
- Match score: 0.76
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/unified-chaos-injection-and-slo-validation-experiments-in-kubernetes/aeTCYm1x-co.txt
- Transcript chars: 20258
- Keywords: experiment, application, cluster, experiments, iterate, testing, metrics, litmus, launch, deployment, easily, running, latency, resiliency, checking, version, conditions, simply

### Resumo baseado na transcript

experiments in kubernetes development time obviously we're going to be writing unit tests for our application we want to make sure that our application is behaving the way we would expect it to behave now no matter which language we use to develop our application we have our favorite unit testing Frameworks it's going to let us write our unit tests easily and execute them easily and get results from them easily now let's say we're taking this application we have developed and deploying it in kubernetes don't you want

### Excerpt da transcript

experiments in kubernetes development time obviously we're going to be writing unit tests for our application we want to make sure that our application is behaving the way we would expect it to behave now no matter which language we use to develop our application we have our favorite unit testing Frameworks it's going to let us write our unit tests easily and execute them easily and get results from them easily now let's say we're taking this application we have developed and deploying it in kubernetes don't you want to test the deployed version of the application of course we do this is where experiments come in so we will simply use the term experiments as a short code for tests that you run for your deployed and running applications that's what an experiment is and we're going to be looking at how you can easily author these experiments and how you can easily execute them and also how you can consume results back from these experiments so I mentioned I'm sure familiar with different types of experiments so the simplest type of experiment is load testing your application so let's say it's a service that you're deploying obviously you want to make sure that it can handle realistic load and it's latency and error related properties are okay even in the midst of a real world load conditions that's a load test experiment let's say you also have a new version of your application you may want a dark launch it or Canary it so you are either sending a copy of the end user traffic to the application to the new version or maybe you're sending a portion of the traffic to the new version and measuring how well it's performing that's an example of it Canary experiment how about resiliency so maybe a part goes down in the class or maybe a node goes down in the cluster and you want to see how the application is holding up in the midst of these instabilities this is where chaos testing comes in so chaos is a way to inject this type of instability in a very controlled manner into the infrastructure and see how your application is performing that's an example of resiliency testing and resiliency experiment and finally there is of course A B testing so maybe you're deploying a machine learning model and maybe the machine learning model is recommending books or socks or news articles or whatever and you want to make sure that you're getting new users you want to make sure that you're increasing your Revenue so essentially a b testing is all about picking the best version of
