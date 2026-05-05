---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "AI + ML"
themes: ["AI ML"]
speakers: ["Sergey Kanzhelev", "Google", "Mrunal Patel", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7pT/navigating-failures-in-pods-with-devices-challenges-and-solutions-sergey-kanzhelev-google-mrunal-patel-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Navigating+Failures+in+Pods+with+Devices%3A+Challenges+and+Solutions+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Navigating Failures in Pods with Devices: Challenges and Solutions - Sergey Kanzhelev, Google & Mrunal Patel, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]]
- País/cidade: United States / Salt Lake City
- Speakers: Sergey Kanzhelev, Google, Mrunal Patel, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7pT/navigating-failures-in-pods-with-devices-challenges-and-solutions-sergey-kanzhelev-google-mrunal-patel-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Navigating+Failures+in+Pods+with+Devices%3A+Challenges+and+Solutions+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Navigating Failures in Pods with Devices: Challenges and Solutions.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7pT/navigating-failures-in-pods-with-devices-challenges-and-solutions-sergey-kanzhelev-google-mrunal-patel-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Navigating+Failures+in+Pods+with+Devices%3A+Challenges+and+Solutions+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-YCnOYTtVO8
- YouTube title: Navigating Failures in Pods with Devices: Challenges and Solutions - Sergey Kanzhelev & Mrunal Patel
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/navigating-failures-in-pods-with-devices-challenges-and-solutions/-YCnOYTtVO8.txt
- Transcript chars: 31692
- Keywords: device, devices, failed, plugin, failure, another, workload, typically, running, workloads, restart, schedule, information, inference, policy, status, working, cannot

### Resumo baseado na transcript

hi you're here for um navigation failures in uh ports with devices we are my name is Serge kelif I'm chair of signode and one of the approvers I work for gke and sometimes on on call for node and many of these no these days uh have accelerators so every time something failed I will know about it and I will dig into that and oh it's a device failed we need to deal something uh with that somehow and um I by no means I'm professional in accelerators

### Excerpt da transcript

hi you're here for um navigation failures in uh ports with devices we are my name is Serge kelif I'm chair of signode and one of the approvers I work for gke and sometimes on on call for node and many of these no these days uh have accelerators so every time something failed I will know about it and I will dig into that and oh it's a device failed we need to deal something uh with that somehow and um I by no means I'm professional in accelerators I don't know much about them but I don't know I I know enough to how they affect kubernetes and Ral uh Hey folks I'm Ral I'm a software engineer at redart I'm one of the tech leads and co-chairs of Sig node and our goal today is to figure out how we can better surface device uh issues from pods and uh better support AIML workloads so motivation like modern workloads use a lot of new devices Beyond just CPU memory and network right you have your accelerator cards you have specialized uh network devices and so on so AI ml training can run for weeks to months so uh any device failures could drastically slow you down and it can be frustrating and we want uh kubernetes to be the platform that can be used uh for all these use cases es so visibility into this device failures and automatic remediation uh is the goal that we want to work towards so uh if folks have seen uh the Llama paper they site that uh during training Lama 78% of the interruptions were due to hardware issues and uh 59% were because of GPU issues so this is like some motivation on why we need to this so you just saw numbers in red right so number in red is how many time device failed and you remember about kubernetes kubernetes is I mean in kubernetes you provision not you barely can change the size of it in CPU and memory and if you have a device you either have it or you don't have it that was a pattern for a very long time and with this pattern like we survived for many years and now with AIML going uh being dominant uh workload that we want to serve it's a change of Paradigm and why would people use kubernetes for this change of Paradigm why people still running on kubernetes if it's not designed for IML like maybe we need to switch to something else uh this question we heard a lot uh especially past year and I think many people already settled on that but I just want to reiterate on that why this talk is even happening why we talking about e IML and kubernetes and not talking about let's build something new some new Frameworks that will know about
