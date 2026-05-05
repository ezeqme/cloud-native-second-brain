---
type: promcon-talk
conference: PromCon
edition: "PromCon EU 2025"
edition_id: 2025-munich
year: 2025
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Metrics", "OpenTelemetry", "Scalability Reliability"]
speakers: ["Pavan Yekbote"]
source_url: https://promcon.io/2025-munich/talks/building-an-observability-agent-for-rapid-root-cause-analysis-using-prometheus-metrics/
youtube_url: https://www.youtube.com/watch?v=q8HLHZQOLCU
youtube_search_url: https://www.youtube.com/results?search_query=Building+an+Observability+Agent+for+Rapid+Root+Cause+Analysis+using+Prometheus+metrics+PromCon+2025
video_match_score: 1.036
status: video-found
---

# Building an Observability Agent for Rapid Root Cause Analysis using Prometheus metrics

## Identificação

- Edição: PromCon EU 2025
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Metrics]], [[OpenTelemetry]], [[Scalability Reliability]]
- Speakers: Pavan Yekbote
- Página oficial: https://promcon.io/2025-munich/talks/building-an-observability-agent-for-rapid-root-cause-analysis-using-prometheus-metrics/
- YouTube: https://www.youtube.com/watch?v=q8HLHZQOLCU

## Resumo

Summary This talk demonstrates how to build a Prometheus-focused observability agent that intelligently analyzes Prometheus metrics alongside supplementary telemetry (logs and traces from OpenSearch) to quickly identify and troubleshoot issues. We present a practical, metrics-driven approach leveraging MCP (Model Context Protocol) servers for smarter, faster root cause analysis. Description Effective observability begins with metrics.

## Abstract oficial

Summary

This talk demonstrates how to build a Prometheus-focused observability agent that intelligently analyzes Prometheus metrics alongside supplementary telemetry (logs and traces from OpenSearch) to quickly identify and troubleshoot issues. We present a practical, metrics-driven approach leveraging MCP (Model Context Protocol) servers for smarter, faster root cause analysis.

Description

Effective observability begins with metrics. However, metrics alone may lack critical context to fully explain incidents. This talk explores a practical solution—a Prometheus-centric observability agent enhanced by correlated telemetry stored in OpenSearch.

We highlight a real-world scenario where metrics are collected using OpenTelemetry and stored in Prometheus, while logs and traces are stored in OpenSearch. The observability agent leverages the Model Context Protocol (MCP) server to intelligently interpret Prometheus metrics and access supplemental telemetry to rapidly pinpoint underlying problems.

The session will highlight:


Architecture of an observability agent designed to utilize Prometheus metrics
Utilizing MCP servers to provide additional contextual insights
A demonstration illustrating rapid root-cause identification and resolution workflows using this metrics-first approach.


Participants will learn actionable strategies to improve observability and significantly reduce mean-time-to-resolution.

## Links

- Página oficial: https://promcon.io/2025-munich/talks/building-an-observability-agent-for-rapid-root-cause-analysis-using-prometheus-metrics/
- YouTube: https://www.youtube.com/watch?v=q8HLHZQOLCU
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=q8HLHZQOLCU
- YouTube title: PromCon 2025 - Building an Observability Agent for Rapid Root Cause Analysis using Prometheus met...
- Match score: 1.036
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2025/building-an-observability-agent-for-rapid-root-cause-analysis-using-pr/q8HLHZQOLCU.txt
- Transcript chars: 31740
- Keywords: llm, metrics, context, search, memory, actually, prometheus, provide, server, agents, logs, itself, perform, traces, application, execute, analysis, history

### Resumo baseado na transcript

Hope you have had a great day today so far listening in on all the sessions. So in today's topic, we'll be looking at and learning how one could leverage the power of agents to perform rapid root cause analysis. Um we'll look into some of the challenges and strategies you can use to uh improve the accuracy of such such agents. You look at some logs, you try to identify why it went wrong, and then you come up with some sort of hypothesis, and done, the root cause has been found. You have metrics, you have logs, traces that probably live in separate systems and do you have the context and the capability to know all these query languages and look and query for the right data to tell you what went wrong. Why don't you also build a system that can read the data, understand it, and give you some guidance on how you can solve such problems, right?

### Excerpt da transcript

Hi everyone. Hope you have had a great day today so far listening in on all the sessions. My name is Pawan. I'm a software development engineer at AWS. I'm also a maintainer of the ML Commons plug-in on open search. So in today's topic, we'll be looking at and learning how one could leverage the power of agents to perform rapid root cause analysis. Right? But before jumping into this, let's take a look at a scenario. Right? I'm sure all of us have been in this situation at some point in our life. Uh you're having a pleasant sleep. You get paged at like 1:00 a.m. or 2:00 a.m. You're on call. You got to wake up. You don't want to wake up, but you got to wake up. you force yourself to get out of bed. You look at some metrics to try and understand what went wrong. Did something really go wrong or was it like a false alarm. Um then you pull up some logs. You pull up some traces, right? You come up with a hypothesis that could have caused the problem. Hopefully you find the root cause. You mitigate the issue and call it a night, right?

But the sleep when you go back is not really convenient cuz you're worried about getting paged again, right? So in this talk, let's focus on, you know, how we can mitigate some of the pain associated with this scenario and how one could potentially make their lives easier, right? If you couldn't tell already, these images were generated using AI, but let's take a look at how you can use AI to do some more. So the agenda for today will be we'll be going over a typical root cause analysis workflow. We'll be looking into agents, some of the building blocks associated with agents. We'll go over a quick demo. Um we'll look into some of the challenges and strategies you can use to uh improve the accuracy of such such agents. We'll look into how this can integrate into the future and how it can help mitigate some of the pain. And then we'll just have a quick Q&A session. So a typical root cause analysis workflow involves something like this, right? An alerts get an alert gets triggered. You look at some metrics, try to identify what went wrong.

You look at some logs, you try to identify why it went wrong, and then you come up with some sort of hypothesis, and done, the root cause has been found. But it's rarely as easy as it seems, right? It's never this easy as it seems. And there's quite a few pain points that are associated with this. Well, first thing is you got to perform complex cross-system reasoning under time pressure, right?
