---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Keynote Sessions"
themes: ["AI ML"]
speakers: ["Maura Kelly", "Mailchimp", "Steven Bower", "Bloomberg", "Adam Kocoloski", "Airbnb", "Liguang Xie", "ByteDance"]
sched_url: https://kccncna2025.sched.com/event/27dEN/keynote-turn-up-the-heat-driving-cloud-native-innovation-into-real-world-impact-maura-kelly-mailchimp-steven-bower-bloomberg-adam-kocoloski-airbnb-liguang-xie-bytedance
youtube_search_url: https://www.youtube.com/results?search_query=Keynote%3A+Turn+Up+the+Heat%3A+Driving+Cloud+Native+Innovation+into+Real-World+Impact+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Keynote: Turn Up the Heat: Driving Cloud Native Innovation into Real-World Impact - Maura Kelly, Mailchimp; Steven Bower, Bloomberg; Adam Kocoloski, Airbnb; Liguang Xie, ByteDance

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Keynote Sessions]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Maura Kelly, Mailchimp, Steven Bower, Bloomberg, Adam Kocoloski, Airbnb, Liguang Xie, ByteDance
- Schedule: https://kccncna2025.sched.com/event/27dEN/keynote-turn-up-the-heat-driving-cloud-native-innovation-into-real-world-impact-maura-kelly-mailchimp-steven-bower-bloomberg-adam-kocoloski-airbnb-liguang-xie-bytedance
- Busca YouTube: https://www.youtube.com/results?search_query=Keynote%3A+Turn+Up+the+Heat%3A+Driving+Cloud+Native+Innovation+into+Real-World+Impact+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Keynote: Turn Up the Heat: Driving Cloud Native Innovation into Real-World Impact.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27dEN/keynote-turn-up-the-heat-driving-cloud-native-innovation-into-real-world-impact-maura-kelly-mailchimp-steven-bower-bloomberg-adam-kocoloski-airbnb-liguang-xie-bytedance
- YouTube search: https://www.youtube.com/results?search_query=Keynote%3A+Turn+Up+the+Heat%3A+Driving+Cloud+Native+Innovation+into+Real-World+Impact+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7KHenRXNGAw
- YouTube title: Keynote: Turn Up the Heat: Driving Cloud Native Innovation into Real-World Impact- Multiple Speakers
- Match score: 0.978
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/keynote-turn-up-the-heat-driving-cloud-native-innovation-into-real-wor/7KHenRXNGAw.txt
- Transcript chars: 15263
- Keywords: platform, inference, infrastructure, source, airbnb, bricks, engineering, developers, cloudnative, workloads, morning, mailchimp, started, bloomberg, projects, running, conference, monolith

### Resumo baseado na transcript

So, um, I work on uh, Mailchimp and my teams kind of keep everything running smoothly. Um, I actually noticed that they were responding to alerts in their Uber on the way to the conference this morning. Luckily for us, in it had already solved a lot of these problems with their development platform. It supports highly available services, boosts developer productivity, and things like compliance, security, and operational excellence are built in. Um, I've always been drawn to building large-scale distributed systems and more importantly making them accessible for engineers. Bloomberg's Kubernetes story started uh in 2016 when coupube 1.3 was just released.

### Excerpt da transcript

Hi, good morning y'all. Uh, my name is Mora Kelly and I'm a director of engineering at Init. Uh, it is great to have you all here in my city. Um, I am sorry we could not order better weather. So, um, I work on uh, Mailchimp and my teams kind of keep everything running smoothly. Um, I actually noticed that they were responding to alerts in their Uber on the way to the conference this morning. [laughter] And uh, today I want to tell you um, a little bit about how we moved Mailchimp onto into its developer platform um, which is built on many of the open source technologies that we're here talking about this conference. So, um, Mailchimp is an email and automations platform and we have 11 million users sending about 700 million emails every day. We were founded in 2001 right here in Atlanta. And this is some pictures of our new office which is about 10 minutes from here. About four years ago, Mailchimp was acquired by Into It and we joined a family of recognizable brands, Turboax, Credit Karma, and QuickBooks.

And we also joined a company very active in the open source community from winning awards to creating the Argo project. So, as you can imagine with any acquisition, we faced a number of tech challenges. We had um additional uh compliance demands with being part of a publicly traded company for the first time. We knew that we wanted a way to bring our products together more easily. Um and we didn't yet have a standard um development uh platform for our services. We were deploying them in different ways. Some were in the cloud and some were actually still on bare metal. Luckily for us, in it had already solved a lot of these problems with their development platform. So, what did we do? A big tech migration. Of course, we started with our biggest project, our 20-year-old monolith. Remember those 11 million users I told you about? They are largely served by this codebase. A joint team from Mailchimp and into it, some of whom are here today, move the monolith onto the in it platform. Uh thanks to the great work of this team and the rockolid technologies underneath, most developers did not even notice it was happening.

We also uh moved some of our existing microservices and even built some new services on the platform. It's great to be coming onto a proven platform. It supports highly available services, boosts developer productivity, and things like compliance, security, and operational excellence are built in. This lets developers focus on building new cus
