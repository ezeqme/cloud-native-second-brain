---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Dolis Sharma", "Nirmata"]
sched_url: https://kccncna2025.sched.com/event/27FW2/real-world-strategies-for-cutting-kubernetes-costs-why-one-size-doesnt-fit-all-dolis-sharma-nirmata
youtube_search_url: https://www.youtube.com/results?search_query=Real-World+Strategies+for+Cutting+Kubernetes+Costs%3A+Why+One+Size+Doesn%E2%80%99t+Fit+All+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Real-World Strategies for Cutting Kubernetes Costs: Why One Size Doesn’t Fit All - Dolis Sharma, Nirmata

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Dolis Sharma, Nirmata
- Schedule: https://kccncna2025.sched.com/event/27FW2/real-world-strategies-for-cutting-kubernetes-costs-why-one-size-doesnt-fit-all-dolis-sharma-nirmata
- Busca YouTube: https://www.youtube.com/results?search_query=Real-World+Strategies+for+Cutting+Kubernetes+Costs%3A+Why+One+Size+Doesn%E2%80%99t+Fit+All+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Real-World Strategies for Cutting Kubernetes Costs: Why One Size Doesn’t Fit All.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FW2/real-world-strategies-for-cutting-kubernetes-costs-why-one-size-doesnt-fit-all-dolis-sharma-nirmata
- YouTube search: https://www.youtube.com/results?search_query=Real-World+Strategies+for+Cutting+Kubernetes+Costs%3A+Why+One+Size+Doesn%E2%80%99t+Fit+All+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=p3r4StwaHWc
- YouTube title: Real-World Strategies for Cutting Kubernetes Costs: Why One Size Doesn’t Fit All - Dolis Sharma
- Match score: 1.003
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/real-world-strategies-for-cutting-kubernetes-costs-why-one-size-doesnt/p3r4StwaHWc.txt
- Transcript chars: 27717
- Keywords: policy, policies, cost, resources, application, workloads, carpenter, solution, instance, cleanup, deployment, strategies, solutions, applications, scaling, request, adding, mutate

### Resumo baseado na transcript

As you may see on the screen which I am not able to but I'm pretty sure you are able to is the topic for today is how do you cut your cost in oneliner but it's going to be more about real world strategies and the reason I'm adding in that when it comes to Kubernetes cloud cost one solution doesn't fit all this is based on talking to many customers, talking to many users, looking at cost optimization and what I've learned so far, I may be wrong, But these are like top three four challenges that I see from time to time. But we'll give you an idea in terms of how to approach this and how to think about reducing your cost. That means if you have bad jobs or you have some crown jobs or you have some applications which are like shooting up really high, you don't know how to scale them. Now you'll say autoscaling is good concept or there is there is this tool that we can do but we don't have entirely the strategies because how do you scale and then scale down and how do you provide the resources but also make sure that you're not overprovisioning it.

### Excerpt da transcript

As you may see on the screen which I am not able to but I'm pretty sure you are able to is the topic for today is how do you cut your cost in oneliner but it's going to be more about real world strategies and the reason I'm adding in that when it comes to Kubernetes cloud cost one solution doesn't fit all this is based on talking to many customers, talking to many users, looking at cost optimization and what I've learned so far, I may be wrong, but what I've learned is the solution that I may propose to one user might not fit for other. And that's why what we are going to do on today's session is I'm going to just throw some solutions that I've been seeing talking to users and then let you decide which one works for your environment because as I say one solution the same solution will not fit everyone. It is depending upon your environment, the nature of your applications, which ones are critical, how the architecture and design is set up is what goes into designing such solutions. What what you expect from today's session is we'll first touch base why your Kubernetes cost is high.

What are some of the primary top three four reasons that you might be seeing a cost spike? Then we're going to talk about some top challenges. And you may have these challenges or you may have something related to these challenges. But these are like top three four challenges that I see from time to time. We'll talk about policydriven solutions for optimization. But it's just not always policies. It's going to be different solutions like Kivero, VPA, different CNCF tools that you can use. But we'll give you an idea in terms of how to approach this and how to think about reducing your cost. And then call to action. What should you do when you're when you're flying back thinking about the session? What should you do next? What should you what should you start exploring? And how do you approach this? Step number one, step number two, etc., etc. Oh, okay. I think the door is closed. I think it's okay. Perfect. So let's let's get into it. I'm seeing a lot of people so I might get a little nervous but that's I think that's okay.

So thank you. So why is your Kubernetes bill so high? First the top most reason is overprovisioning workloads. Sometimes we just get really too excited about our workloads or probably we have a pressure that you know if you provide less resources probably they'll end up having CPU throttling issues or something else. So we just add all the all the CPUs and m
