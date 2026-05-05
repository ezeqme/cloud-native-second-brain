---
type: kubecon-session
event: "KubeCon + CloudNativeCon China 2025 - Hong Kong, China"
event_id: kccncchn2025
year: 2025
region: "China"
city: "Hong Kong"
country: "China"
event_date: "2025"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Yash Bhatnagar", "Google"]
sched_url: https://kccncchn2025.sched.com/event/1x5jb/kube-intelligence-a-metric-based-insightful-remediation-recommender-yash-bhatnagar-google
youtube_search_url: https://www.youtube.com/results?search_query=Kube+Intelligence+-+A+Metric+Based+Insightful+Remediation+Recommender+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kube Intelligence - A Metric Based Insightful Remediation Recommender - Yash Bhatnagar, Google

## Identificação

- Edição: KubeCon + CloudNativeCon China 2025 - Hong Kong, China
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: China / Hong Kong
- Speakers: Yash Bhatnagar, Google
- Schedule: https://kccncchn2025.sched.com/event/1x5jb/kube-intelligence-a-metric-based-insightful-remediation-recommender-yash-bhatnagar-google
- Busca YouTube: https://www.youtube.com/results?search_query=Kube+Intelligence+-+A+Metric+Based+Insightful+Remediation+Recommender+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kube Intelligence - A Metric Based Insightful Remediation Recommender.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncchn2025.sched.com/event/1x5jb/kube-intelligence-a-metric-based-insightful-remediation-recommender-yash-bhatnagar-google
- YouTube search: https://www.youtube.com/results?search_query=Kube+Intelligence+-+A+Metric+Based+Insightful+Remediation+Recommender+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Ef1DisgzlwE
- YouTube title: Kube Intelligence - A Metric Based Insightful Remediation Recommender - Yash Bhatnagar, Google
- Match score: 0.939
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kube-intelligence-a-metric-based-insightful-remediation-recommender/Ef1DisgzlwE.txt
- Transcript chars: 22489
- Keywords: applications, network, metrics, serverless, application, average, latency, across, resource, certain, moving, several, optimizations, recommendations, around, analysis, cost, resources

### Resumo baseado na transcript

Today I'll be discussing a case study on how leveraging a right set of metrics can help you solve a wide variety of problems related to managing your applications in Kubernetes and how we built an internal tool that help us achieve the same at a planet scale. So as we know Kubernetes provides several configuration constructs like limits, priority classes, jobs, chron jobs etc. The real challenge occurs when you have a large organization like you have several independent products in different stages of your life cycle. As an example, if you have a wide global product with good revenues, you would naturally tend towards maybe investing your crucial bandwidth in something like latency and replication optimizations, but not something very invasive like maybe entire rearchitecture into serverless even though that may still be relevant. Now despite so offer all these challenges what if there was a common platform that can do this for repeated heavy usage of data and analysis for us and it can provide some kind of recommendations which may be specifically useful for the applications owners which are going to be taking actions on them. The idea is that it could generate some kind of predefined optimizations using these collected metrics and the expectation is that it could be something like modular where if you have more such customizations and more such logic that needs to be...

### Excerpt da transcript

All right. Hello everyone. Uh, thanks for joining the session. I'm Yash. I work with the photos team at Google. Today I'll be discussing a case study on how leveraging a right set of metrics can help you solve a wide variety of problems related to managing your applications in Kubernetes and how we built an internal tool that help us achieve the same at a planet scale. So as we know Kubernetes provides several configuration constructs like limits, priority classes, jobs, chron jobs etc. The idea is that the developers can optimize their infrastructure with these constructs based on the requirements that they have or the use that they may have. Now setting them one time is fine but as you know use cases change customers and the patterns change nothing remains the same meaning this often becomes like a ongoing effort and in a sense these optimizations do take a lot of analysis of data time rearchitectures and often they are a big investment of your software engineering bandwidth. So because of that more often than not these optimizations end up taking a backseat first because of these fastpaced CI/CD models where you need to get something out to your customers but once you have reached your customers there are hundreds of thousands of metrics and even more data analysis to be done.

So that is one big problem that you already have and with no insights like maybe performance or cost savings possible there's even lesser motivation to do so. Now suppose despite all of that you do want to invest in optimizing the things that you may have. The real challenge occurs when you have a large organization like you have several independent products in different stages of your life cycle. Hence the kind of optimizations that are relevant to each of these products would be different. As an example, if you have a wide global product with good revenues, you would naturally tend towards maybe investing your crucial bandwidth in something like latency and replication optimizations, but not something very invasive like maybe entire rearchitecture into serverless even though that may still be relevant. On the other hand, maybe a early stage PC product would be interested in both of these, but at the time they don't have enough bandit cruis separately. A lot of commonly used optimizations may end up being done by both of these kind of uh teams and unless it's a perfect cross collaboration and the things have been done in a generic way, they are reusable, it will almost always be
