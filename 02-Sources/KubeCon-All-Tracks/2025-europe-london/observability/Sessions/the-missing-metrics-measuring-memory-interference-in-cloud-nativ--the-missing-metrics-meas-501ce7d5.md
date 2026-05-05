---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Observability"
themes: ["Observability"]
speakers: ["Jonathan Perry", "Unvariance"]
sched_url: https://kccnceu2025.sched.com/event/1txI7/the-missing-metrics-measuring-memory-interference-in-cloud-native-systems-jonathan-perry-unvariance
youtube_search_url: https://www.youtube.com/results?search_query=The+Missing+Metrics%3A+Measuring+Memory+Interference+in+Cloud+Native+Systems+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Missing Metrics: Measuring Memory Interference in Cloud Native Systems - Jonathan Perry, Unvariance

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United Kingdom / London
- Speakers: Jonathan Perry, Unvariance
- Schedule: https://kccnceu2025.sched.com/event/1txI7/the-missing-metrics-measuring-memory-interference-in-cloud-native-systems-jonathan-perry-unvariance
- Busca YouTube: https://www.youtube.com/results?search_query=The+Missing+Metrics%3A+Measuring+Memory+Interference+in+Cloud+Native+Systems+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Missing Metrics: Measuring Memory Interference in Cloud Native Systems.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txI7/the-missing-metrics-measuring-memory-interference-in-cloud-native-systems-jonathan-perry-unvariance
- YouTube search: https://www.youtube.com/results?search_query=The+Missing+Metrics%3A+Measuring+Memory+Interference+in+Cloud+Native+Systems+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nXdGXdxmWNQ
- YouTube title: The Missing Metrics: Measuring Memory Interference in Cloud Native Systems - Jonathan Perry
- Match score: 0.987
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-missing-metrics-measuring-memory-interference-in-cloud-native-syst/nXdGXdxmWNQ.txt
- Transcript chars: 28885
- Keywords: neighbor, memory, performance, application, workloads, systems, applications, latency, bandwidth, measure, better, collector, running, question, millisecond, neighbors, production, contention

### Resumo baseado na transcript

I want to start with a few snapshots from this YouTube video called positive affirmations for site reliability engineers. A lone SRE is sitting at his desk looking at exceptions in production and the rising cost of the deployment. And as our systems become more and more complex, it becomes harder to reason about performance. And it's easy when performance degrade to blame the spaghetti monster of complexity or the network. But really a lot of that uh degradation in performance comes from simple resource congestion on the server that we just have no visibility into. Over more than a decade, there have been more than a dozen papers by well-known research universities and our hyperscalers that explore this capability and uh and give us detail on how to mitigate these noisy neighbors.

### Excerpt da transcript

Hi everybody. Welcome to this talk about memory noisy neighbor. I hope you're all caffeinated and ready to go. I want to start with a few snapshots from this YouTube video called positive affirmations for site reliability engineers. I highly recommend you watch it. It starts at night. A lone SRE is sitting at his desk looking at exceptions in production and the rising cost of the deployment. He's feeling so frustrated and haggarded. He meditates. A calm female voice tells him, "Your pipeline is green. Your tests are well written and stable. your friends and family understand what you do. You were born to deploy Kubernetes clusters. And so this got me thinking, why do we take on this heroic task of maintaining these large deployments? And for me, the ultimate affirmation is this. Your deployment is highly available and costefficient. Users delight in the product and its performance. And this is the holy grail what we all strive towards and performance that uh part of our holy grail really matters and both companies understand uh the importance both to users the user experience and their bottom line.

Uh Amazon released a case study uh saying that for every 100 millisecond increase in uh user response times they lose 1% of revenue. And there have been dozens of case studies over the years uh reinforcing those results. I only were was able to bring just a few of the highc caliber names I was I found. Uh, one of the one of the uh, case studies I really liked is this one by Raku 1024, which is a Japanese online grocery where they ran an AB test and they ran two applications with exactly the same functionality, but one of them was optimized and ran 400 milliseconds faster and they had startling results from the faster application. It increased revenue per user by 53% and reduced bounce rates by 35%. So performance really matters. But with that users also expect better functionality. And your systems might not be as complex as these extreme examples of service maps published by big companies but still uh your systems are probably quite complex. users expect uh better functionality, right? They recom better better recommendations, search engines, maybe AI, and in general just a more featureful application.

And as our systems become more and more complex, it becomes harder to reason about performance. And it's easy when performance degrade to blame the spaghetti monster of complexity or the network. But really a lot of that uh degradation in performance comes from
