---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Operations + Performance"
themes: ["GitOps Delivery", "SRE Reliability"]
speakers: ["Angela Victorio", "JP Morgan Chase"]
sched_url: https://kccncna2025.sched.com/event/27FVh/taming-rollout-risks-in-distributed-web-apps-a-location-aware-gradual-deployment-approach-angela-victorio-jp-morgan-chase
youtube_search_url: https://www.youtube.com/results?search_query=Taming+Rollout+Risks+in+Distributed+Web+Apps%3A+A+Location-Aware+Gradual+Deployment+Approach+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Taming Rollout Risks in Distributed Web Apps: A Location-Aware Gradual Deployment Approach - Angela Victorio, JP Morgan Chase

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Operations + Performance]]
- Temas: [[GitOps Delivery]], [[SRE Reliability]]
- País/cidade: United States / Atlanta
- Speakers: Angela Victorio, JP Morgan Chase
- Schedule: https://kccncna2025.sched.com/event/27FVh/taming-rollout-risks-in-distributed-web-apps-a-location-aware-gradual-deployment-approach-angela-victorio-jp-morgan-chase
- Busca YouTube: https://www.youtube.com/results?search_query=Taming+Rollout+Risks+in+Distributed+Web+Apps%3A+A+Location-Aware+Gradual+Deployment+Approach+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Taming Rollout Risks in Distributed Web Apps: A Location-Aware Gradual Deployment Approach.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FVh/taming-rollout-risks-in-distributed-web-apps-a-location-aware-gradual-deployment-approach-angela-victorio-jp-morgan-chase
- YouTube search: https://www.youtube.com/results?search_query=Taming+Rollout+Risks+in+Distributed+Web+Apps%3A+A+Location-Aware+Gradual+Deployment+Approach+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-fhXEJD-ycs
- YouTube title: Taming Rollout Risks in Distributed Web Apps: A Location-Aware Gradual Deployment... Angela Victorio
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/taming-rollout-risks-in-distributed-web-apps-a-location-aware-gradual/-fhXEJD-ycs.txt
- Transcript chars: 17548
- Keywords: version, change, machine, script, deployment, actually, changes, machines, deploy, request, profile, production, feature, everything, percentage, automated, gradual, software

### Resumo baseado na transcript

Uh previously I was working for American Airlines and my demos are more related to my experience with American Airlines. I have been doing software development uh CI/CD pipeline and the past few years I've been working with the Kubernetes and we all know that Kubernetes is a good it eliminate the downtime during deployment but you know as long as the software exist there will be software bugs. the other region and today I'm mostly going to talk about this um service mesh um I'm using as the example so um it's mostly do um based um I have my demo site tab uh because I don't trust how the Wi-Fi speed is Okay, about this demo one uh I'm going to quickly show DO one is the very basic feature of East it can do those weighted uh routing based on percentage. So, for that to do, you'll see my my demo is pretty simple is using ngx uh and I just have a uh index html page. So for this demo two um we can do some really granular control through um like a still through east but east traffic routing it has another feature it can route traffic uh based on the request hider.

### Excerpt da transcript

Hello everyone. My name is Angela Victoria. Thank you for attending my session. Uh I'm a technical lead uh at JP Morgan Chase. Uh previously I was working for American Airlines and my demos are more related to my experience with American Airlines. I have been doing software development uh CI/CD pipeline and the past few years I've been working with the Kubernetes and we all know that Kubernetes is a good it eliminate the downtime during deployment but you know as long as the software exist there will be software bugs. Most of the time uh it could be just some type of defects. Your application still running there are certain scenario then it's not behaving as expected then it's okay you just fix forward and do another deployment to fix that. But once a while if you have a uh that type of experience some very simple code change very naive code change it just create a disaster and you don't want that ever to happen in your production whatever the reason that got pushed to production why that wasn't caught during testing or in your lower environment I'm not going to get into that but I'm just saying like for you to do deployment uh you should think about now to roll out just 100% you need to reduce this blast radius.

Let me ask a question. Uh how many of you do some sort of canary deployment? Yeah, I see quite a few of those. And then we want to make deployment our release boring. So for that you shouldn't have any type of anxiety. What if my testing was not enough or something like just went out to production and just break my application? If data happens, think about I only deploy 10%. You are only impacting 10% of your users not 100%. that greatly reduce the impact of those type of defect. And for graduate roll out, there are all different ways of doing that like using feature flex um is a pretty common or you can have a some type of a code logic just for example a new feature. I use a code to control now to row it out or I can have a feature flag um in my config map like I can enable in one region not in the other region then that's just 50%. Uh let me ask how many of you use some type of uh some um type of feature switch. Yes. Um so I know this is pretty common and then the other ways to control that you can use some uh DNS based um those type of traffic splitting or just very simple way you don't have to invise anything redo your CI/CD pipelines if you have a multiple cluster or you have a uh let's see you have a two regions just deploy to one region bu
