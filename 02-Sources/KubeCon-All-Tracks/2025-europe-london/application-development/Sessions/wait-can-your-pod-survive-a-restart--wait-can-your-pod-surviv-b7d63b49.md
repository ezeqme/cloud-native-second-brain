---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["AI ML"]
speakers: ["Aya Ozawa", "CloudNatix Inc."]
sched_url: https://kccnceu2025.sched.com/event/1txEp/wait-can-your-pod-survive-a-restart-aya-ozawa-cloudnatix-inc
youtube_search_url: https://www.youtube.com/results?search_query=Wait%21+Can+Your+Pod+Survive+a+Restart%3F+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Wait! Can Your Pod Survive a Restart? - Aya Ozawa, CloudNatix Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]]
- País/cidade: United Kingdom / London
- Speakers: Aya Ozawa, CloudNatix Inc.
- Schedule: https://kccnceu2025.sched.com/event/1txEp/wait-can-your-pod-survive-a-restart-aya-ozawa-cloudnatix-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Wait%21+Can+Your+Pod+Survive+a+Restart%3F+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Wait! Can Your Pod Survive a Restart?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEp/wait-can-your-pod-survive-a-restart-aya-ozawa-cloudnatix-inc
- YouTube search: https://www.youtube.com/results?search_query=Wait%21+Can+Your+Pod+Survive+a+Restart%3F+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=eO8szEGNwoo
- YouTube title: Wait! Can Your Pod Survive a Restart? - Aya Ozawa, CloudNatix Inc.
- Match score: 0.817
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/wait-can-your-pod-survive-a-restart/eO8szEGNwoo.txt
- Transcript chars: 17300
- Keywords: signal, traffic, application, container, shutdown, restart, period, eviction, request, startup, handle, controller, duration, default, replica, deployment, however, requests

### Resumo baseado na transcript

Potter restarts might sound basic, but handling them correctly is a bit challenging. And if your pot isn't ready for prepare for that, you could run into unexpected issues. The sidecore design pattern which is extend the functionality of the primary container like logging agents like that has been known for many years but cyto support as a native kubernetes feature is relatively new. And even when Kubernetes does to do termination, it can sometime be overridden or ignored. When you delete a port, Kubernetes sends a stop signal as we learned before then eventually removes a port from the routing table. To avoid this problem, shutdown should be delayed until Kubernetes stop routing traffic to the pot.

### Excerpt da transcript

Hello everyone. Thank you for so much for joining my session today. Let me ask you a quick question. Can you put survival restart? Potter restarts might sound basic, but handling them correctly is a bit challenging. Kubernetes restart port in many situations. And if your pot isn't ready for prepare for that, you could run into unexpected issues. Before we dive in, let me briefly introduce myself. My name is Ay Zawa. I'm member of technical staff at Crownatics. I'm currently developing L Marina. It's a open source AI platform for Kubernetes. So today I going to show you some insights I learned over the years. Here is the today's agenda. I going to show you how to reduce the impact of restart using three different type of application as example. Let's move on. So why does restart matter? It comes down how Kubernetes traits your app. You might have heard the famous analogy, Kubernetes treats you up more like cattle rather than pet. But what does mean? If your application is a pet, it requires special care manual intervention every time it goes wrong.

But Kubernetes is optimized for cattle. In fact, many powerful features such as self-heering, roaring upgrade and autocaring fundamentally rely on restarts. So take out take advantage of those powerful features. Put restartability as important. A restart isn't just a single scenario. We'll dive into the detail later but for now let's get a high level overview at the container level if your container exit or livveness prove failure the kubert restarted and second at the replica set level even if your part gets the readed it automatically recreated by the controller to keep the desired replica count at the deployment level during ing a roaring up degrade. Unlike the previous two scenarios, deployment creates a new port forest before degrading the old one. So, how can we ensure our workloads survive in these scenarios? Let's examine the simplest scenario, a basic duration and recreation flow. We have a simple deployment. This defined only image and arguments but doesn't handle any signals. Let's say we direct its pot using cubic cut direct pot for three this port receive a stop signal usually six time.

However, if the application doesn't handle the signal, it continue running during the default 30 grace period. Once that time is up, the port is forcibly stopped with sig kill. Meanwhile, the number of running port drops below the desired number. So the port is recreated. Then scheduling, image brewing and container
