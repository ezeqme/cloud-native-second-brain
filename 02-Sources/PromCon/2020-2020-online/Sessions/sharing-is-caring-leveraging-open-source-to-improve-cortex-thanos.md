---
type: promcon-talk
conference: PromCon
edition: "PromCon Online 2020"
edition_id: 2020-online
year: 2020
city: "Online"
country: "Online"
topics: ["Prometheus Core", "Metrics", "Remote Write Storage", "Scalability Reliability", "Community"]
speakers: []
source_url: https://promcon.io/2020-online/talks/sharing-is-caring--leveraging-open-source-to-improve-cortex---thanos/
youtube_url: https://www.youtube.com/watch?v=2oTLouUvsac
youtube_search_url: https://www.youtube.com/results?search_query=Sharing+is+Caring%3A+Leveraging+Open+Source+to+Improve+Cortex+%26+Thanos+PromCon+2020
video_match_score: 0.997
status: video-found
---

# Sharing is Caring: Leveraging Open Source to Improve Cortex & Thanos

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus Core]], [[Metrics]], [[Remote Write Storage]], [[Scalability Reliability]], [[Community]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/sharing-is-caring--leveraging-open-source-to-improve-cortex---thanos/
- YouTube: https://www.youtube.com/watch?v=2oTLouUvsac

## Resumo

Speaker: Bartłomiej Płotka Speaker: Marco Pracucci Perhaps some of the success of the original Prometheus project can be attributed to the desire to keep it simple: no dependencies, no trendy distributed systems, a single binary with a simple mission. This approach left some problems unsolved - how do you scale your Prometheus installation across multiple sites? How do you ensure your metrics are durably stored for long term analysis?

## Abstract oficial

Speaker: Bartłomiej Płotka
Speaker: Marco Pracucci

Perhaps some of the success of the original Prometheus project can be attributed to the desire to keep it simple: no dependencies, no trendy distributed systems, a single binary with a simple mission.

This approach left some problems unsolved - how do you scale your Prometheus installation across multiple sites? How do you ensure your metrics are durably stored for long term analysis? And how do you build a monitoring system that can transparently tolerate machine failure?

Once upon a time, two open source projects were created to solve those problems at scale: Cortex and Thanos. Originally designed with a totally different architecture and trade-offs but for the same goals. Because of open source, over time, both projects were observing and started to learn from each other. Both started influencing each other with ideas and improvements. Today Cortex and Thanos are closer than ever, with a tight collaboration which is making their architectures converge and evolve, significantly improving both projects and influencing the Prometheus ecosystem on the way!

In this talk, you will learn why those two potentially competing CNCF projects are working together and where this is heading! Marco (Cortex maintainer)and Bartek (Thanos co-author) will explain how Cortex and Thanos leverage open source to collaborate better, without introducing maintenance burden. We will cover the cutting edge state of both projects and the most recent wins thanks to the joint effort, showing the pillars of the open source: sharing and caring!

## Links

- Página oficial: https://promcon.io/2020-online/talks/sharing-is-caring--leveraging-open-source-to-improve-cortex---thanos/
- YouTube: https://www.youtube.com/watch?v=2oTLouUvsac
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2oTLouUvsac
- YouTube title: PromCon Online 2020 - Sharing is Caring: Leveraging Open Source to Improve Cortex & Thanos
- Match score: 0.997
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/sharing-is-caring-leveraging-open-source-to-improve-cortex-thanos/2oTLouUvsac.txt
- Transcript chars: 27300
- Keywords: cortex, thanos, storage, projects, collaboration, single, prometheus, tunnels, especially, question, working, together, definitely, source, learned, however, actually, competition

### Resumo baseado na transcript

[Music] i would like to share with you a personal story uh ten months ago i was leaving my previous job to join graphene labs and focus on cortex development before that i've never contributed much to open source and i feel the i feel i've learned a lot over the past few months and the most important lesson i learned about open source is that open source is not about technology and actually open source is all about people and to me personally open source is one of the

### Excerpt da transcript

[Music] i would like to share with you a personal story uh ten months ago i was leaving my previous job to join graphene labs and focus on cortex development before that i've never contributed much to open source and i feel the i feel i've learned a lot over the past few months and the most important lesson i learned about open source is that open source is not about technology and actually open source is all about people and to me personally open source is one of the most beautiful expressions of collaboration um think about it a group of very diverse people coming from all over the world working together on a single project and giving back this project to a wider community and in this talk we would like to to share with you the story behind a stronger collaboration between cortex and toms hi everyone my name is marker i'm a software engineer at grafana labs i'm a cortex maintainer and i'm recently joined the time maintainers as well thanks marco um so my name is bartlett vodka and i'm a software engineer at red hat in the monitoring team i'm pirate of the prometheus team as well and co-author of thanos project i also you might know me from the newly created cncf seek observability which you can find on our more details on our repo please join us so today we will be kind of continuing the talk that we made with tom wilkie who is culture of cortex a year ago nearly a year ago on the prom con in munich last year and we were talking about those two projects we introduced them and we talked about the differences and similarities um around those and as you maybe know those projects aims for kind of the same goal which is global view of your metrics of your promote use metrics maybe durable view so you can also handle some kind of aha of replicas of from it uses um and last but not the least long-term storage retention so in during this talk we'll continue on the on this base however let's briefly talk what we mentioned during that talk you can watch rewatch this talk from the last year for more details and essentially the tldr is that in the beginning especially in the beginning those projects were different on those kind of free simplified dimensions cortex was mainly push-based where you were configuring promoters to push the data um to some centralized clusters uh versus versus internals you are rather pulling the data and querying directly from the prompt users um cortex aimed for different databases um so nosql for index and object storage for um for comp
