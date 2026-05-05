---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting", "Kubernetes", "Scalability Reliability"]
speakers: ["Joel Verezhak"]
source_url: https://promcon.io/2025-munich/talks/alertmanager-has-amnesia--should-we-fix-it/
youtube_url: https://www.youtube.com/watch?v=DwWF6XpyQ0k
youtube_search_url: https://www.youtube.com/results?search_query=Alertmanager+Has+Amnesia+%E2%80%93+Should+We+Fix+It%3F+PromCon+2025
video_match_score: 0.993
status: video-found
---

# Alertmanager Has Amnesia – Should We Fix It?

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]], [[Kubernetes]], [[Scalability Reliability]]
- Speakers: Joel Verezhak
- Página oficial: https://promcon.io/2025-munich/talks/alertmanager-has-amnesia--should-we-fix-it/
- YouTube: https://www.youtube.com/watch?v=DwWF6XpyQ0k

## Resumo

When Alertmanager is rebooted, it loses its understanding about the current "state of the world", i.e. which alerts are actively firing. This is by design, and is in principle no bad thing - Prometheus rules are typically evaluated by multiple replicas of ruler components every 60 seconds, meaning a constant flow of alerts are hitting Alertmanager.

## Abstract oficial

When Alertmanager is rebooted, it loses its understanding about the current "state of the world", i.e. which alerts are actively firing. This is by design, and is in principle no bad thing - Prometheus rules are typically evaluated by multiple replicas of ruler components every 60 seconds, meaning a constant flow of alerts are hitting Alertmanager. Under ideal conditions, this allows the system to quickly reconstruct the "state of the world".

However, in production, life is never quite so simple. Network calls are unreliable by nature, - packets go missing or (more likely) DNS hiccups occur, resulting in alerts not reaching their destination. In high volume environments, these intermitten failures can pile up, leading to a significant gaps in Alertmanager's perception of the alerting landscape.

The complexity increases significantly once we cluster Alertmanager instances for high availability. Each member of the cluster takes turns being the leader, responsible for deciding which notifications need to be shipped to downstream systems. This dynamic introduces numerous race conditions and edge cases, which can lead to unexpected or undesirable behaviour such as duplicate notifications, or missing resolved alerts.

Recently, engineers in our team took part in a hackathon where we played around with a simple idea: what if Alertmanager maintained a shared external view of its state of the world, that persisted across restarts? This is not a new idea - in fact etcd was proposed as a potential backend for such a shared store as far back as 2019.

With the increase in adoption of the Prometheus ecosystem since then, perhaps it is time to revisit and reconsider this approach. In this talk, we'll outline the details of what we hacked together, explore our motivations, and provide an update on progress we made since.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/alertmanager-has-amnesia--should-we-fix-it/
- YouTube: https://www.youtube.com/watch?v=DwWF6XpyQ0k
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DwWF6XpyQ0k
- YouTube title: PromCon 2025 - Alertmanager Has Amnesia – Should We Fix It?
- Match score: 0.993
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/alertmanager-has-amnesia-should-we-fix-it/DwWF6XpyQ0k.txt
- Transcript chars: 37627
- Keywords: manager, alerts, actually, basically, notification, cluster, notifications, another, already, reboot, seconds, gossip, number, happens, interesting, firing, around, interval

### Resumo baseado na transcript

Um, as you see, the talk is called Alert Manager has amnesia with a hidden subheading, shall we fix it? I realized that that's a bit provocative heading, so I I I removed it and you'll see why at the end of the talk. Um so who's actually had like direct experience working with alert manager kind of like an end user like an operator? So this will be like revision for most of you, but then also I think the rest of you this is kind of interesting to see um like a users's perspective of what it's like to work with alert manager. So for example in our production system we have maybe 10,000 alerts firing sometimes even more. If every single one of those alerts resulted in a notification that you had to do something about you'd basically spend your entire day responding and triaging alerts.

### Excerpt da transcript

[music] [clears throat] Okay. Um, thank you so much for the invitation to my first prom. Uh, super super excited to be here. Um, as you see, the talk is called Alert Manager has amnesia with a hidden subheading, shall we fix it? I realized that that's a bit provocative heading, so I I I removed it and you'll see why at the end of the talk. Um, I'm doing this. There's a QR code there. Like, if you want to, you can scan it and like follow along on your phone. I've never tried that before, but it's up to you. You can also call it here. Okay. Um, a bit of background to this talk. So, I'm a systems engineer at Open Systems, but only for the next week or so. I'm actually leaving. Um, so this is a bit of a kind of cathartic talk where I sort of write my memoirs about my time with alert manager. Um, it's one of the tools that we introduced to our stack. Um, it was a big change. It was a big migration and I think I don't think there's any colleagues of mine in here, but I'm not sure I could honestly say it would be 100% good feedback, but it was, you know, we introduced some cool new stuff.

Um, so yeah, this talk is really about kind of um, digging into what alert manager does. um finding a few kind of gotchas and at the end I'll sort of introduce a kind of a hacky thing that we did um just to sort of open the discussion as to sort of the future of where alert manager can go. Okay. Um so who's actually had like direct experience working with alert manager kind of like an end user like an operator? I can see few hands. Okay. Yeah, that's good actually. That's good. So this will be like revision for most of you, but then also I think the rest of you this is kind of interesting to see um like a users's perspective of what it's like to work with alert manager. Um so what does it do? I mean it manages alerts like what does that mean? So for example in our production system we have maybe 10,000 alerts firing sometimes even more. If every single one of those alerts resulted in a notification that you had to do something about you'd basically spend your entire day responding and triaging alerts.

So, alert manager is all about grouping um alerts to make the the number of notifications that you get manageable. It's about rooting. So, making sure that the right team gets notified when their service is broken. Um and you can also do other fancier things like inhibition um and silencing, which we'll dive into much later. At Open Systems, um we're big Thanos users. Um I've giv
