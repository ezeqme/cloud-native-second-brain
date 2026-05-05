---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2022"
edition_id: 2022-munich
year: 2022
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "Alerting", "Scalability Reliability", "Cost Optimization"]
speakers: []
source_url: https://promcon.io/2022-munich/talks/alerting-with-confidence/
youtube_url: https://www.youtube.com/watch?v=OWZU3S44ss0
youtube_search_url: https://www.youtube.com/results?search_query=Alerting+with+Confidence+PromCon+2022
video_match_score: 0.88
status: video-found
---

# Alerting with Confidence

## Identificação

- Edição: PromCon EU 2022
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[Alerting]], [[Scalability Reliability]], [[Cost Optimization]]
- Speakers: N/A
- Página oficial: https://promcon.io/2022-munich/talks/alerting-with-confidence/
- YouTube: https://www.youtube.com/watch?v=OWZU3S44ss0

## Resumo

Speaker(s): Xintao LAI Alerts are hard to set and manage: when we set an alert, we would doubt ourselves, did I set the alert with the correct threshold? Will my alert fire correctly when something goes wrong? Which labels will my alert have?

## Abstract oficial

Speaker(s): Xintao LAI

Alerts are hard to set and manage: when we set an alert, we would doubt ourselves, did I set the alert with the correct threshold? Will my alert fire correctly when something goes wrong? Which labels will my alert have? Who will receive the alerts? And when we received an alert, we will wonder, what does this alert mean? How bad is it?

I'd like to share our way of managing alerts. In Shopee, we use git to manage our alert rules (GitOps). Everyone can change or add an alert by submitting a Pull Request, and then we will review the changes as we do for code. However, it's still hard to review an alert if you are not familiar with the system's insights (the target you are monitoring), to solve that, our CI will replay the alert rules against the production metrics for the past 30 days, CI will report: how many times will the alert be triggered and which groups will be paged (using a tool config routes test). So everyone can get a picture of the changes. It's like a code coverage report (https://about.codecov.io/) for alerts.

To give more information to the receiver when an alert fires, the alert will be sent with a metrics chart that can tell what's going on. To do that, we will parse the alert rules into multiple expressions and render each expression (https://github.com/laixintao/promqlpy/). For example, an alert rule like "CPU > 0.8 or memory < 0.5", will render into 2 pictures that can tell you which of exactly CPU or memory triggered the alert. To make the on-call process more efficient.

## Links

- Página oficial: https://promcon.io/2022-munich/talks/alerting-with-confidence/
- YouTube: https://www.youtube.com/watch?v=OWZU3S44ss0
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OWZU3S44ss0
- YouTube title: PromCon EU 2022: Alerting with Confidence
- Match score: 0.88
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2022/alerting-with-confidence/OWZU3S44ss0.txt
- Transcript chars: 14446
- Keywords: manager, alerts, everything, question, prompt, threshold, little, column, change, receive, review, request, called, normally, render, information, syntax, changes

### Resumo baseado na transcript

[Music] foreign [Music] I'm really sorry that I can't attend the meeting in person but I hope that you like this talk um um my name is Shinto you can find me in Twitter on GitHub using this ID and my Sie as I receive a lot of alert and I don't like them so today without going to talk about how can we make them less annoying we will talk about how to set up a little rules with confidence and how to fire a lot with more information

### Excerpt da transcript

[Music] foreign [Music] I'm really sorry that I can't attend the meeting in person but I hope that you like this talk um um my name is Shinto you can find me in Twitter on GitHub using this ID and my Sie as I receive a lot of alert and I don't like them so today without going to talk about how can we make them less annoying we will talk about how to set up a little rules with confidence and how to fire a lot with more information and how to beat review alerts let's dive into the first part how to set up a lot of rules with confidence um if you have ever set up a little rules I think you will ask those questions to yourself for example did I use the syntax rules correctly and you don't want to break the whole letter uh literal configuration I'm just missing a column in the armor and is this right for the reasonable and they will how many times will my blood Define their reading will somebody be spammed by my alerts for the transport was too low or um uh to be more worse the loss won't be fired if there is something going wrong because the flashcode was too high and who will receive this route and what if my all of what if all of my laws are all set but later someone breaks them just changes some labels and uh or thresholds uh the answer to this question is the CI um to its uh before we dying to see I I need to explain that we use git Ops to manage of our uh a lot rules the key Loops means that we put everything into a kid repository on everything about the monitor observability for example the targets the service Discovery for properties and a lot rules the ultra routine is alert manager the cool thing about Gator Ops is that everything is in git you can check the changes in git commit git commit history you can use Guild clip command command under the reward drawback is very easy and you can review the changes like you're reviewing the code everybody is very familiar with the pull requests the UI and the merge request UI under CM will test everything for you that's that's the main part of our today's topic and there is no magic under the hood everything is here called uh repository if you want to know how is something works you can just check the the code and in kit you can use your favorite Editor to edit everything yes I mean we and the the downside of using it reports uh using githubs is uh it's not very user friendly as web UI some company has a uh has a wrapper around the relative was it's a web UI you can just creating or editing existing electrodes
