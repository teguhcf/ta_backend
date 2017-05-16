#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
entry_points section in setup.cfg:

    console_scripts =
     fibonacci = ta_backend.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from flask import Flask,json,jsonify,request
application = Flask(__name__)

@application.route("/api/v1/onlinereputation/volume/get",methods=['GET'])
def getOnlineReputationbasedonVolume():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'total':10000
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/onlinereputation/diversity/get",methods=['GET'])
def getOnlineReputationbasedonDiversity():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'total_text':10000,
                'total_media':5000,
                'total_extended_entities':4000
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/onlinereputation/validation/get",methods=['GET'])
def getOnlineReputationbasedonValidation():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'total_sentiment_pos':10000,
                'total_sentiment_neg':5000
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/onlinereputation/relevance/get",methods=['GET'])
def getOnlineReputationbasedonRelevance():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'starbucks':["good","delicious"]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/customerneeds/overall",methods=['GET'])
def getCustomerNeedsOverall():
    try:
        time_from=request.args.get('time_from')
        time_to=request.args.get('time_to')
        machineDetail = {
                'positive':["frapucino","starbucks"],
                'negative':["service","starbucks acai"]
                }
        #return json.dumps(machineDetail)
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/customerneeds/sentimentwordsperaspect",methods=['GET'])
def getCustomerNeedsSentimentWordsperAspect():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        aspect=request.args.get('aspect')
        sentiment=request.args.get('sentiment')
        page=request.args.get('page')
        machineDetail = {
                'starbucks':["good","delicious"]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/communityengagement/tweetengagement/get",methods=['GET'])
def getCommunityEngagementTweetEngagement():
    try:
        tweet_id=request.args.get('tweet_id')
        machineDetail = {
                'tweet':{
                    'created_at':"Fri May 05 03:35:21 +0000 2017",
                    'tweet_id_str':"250075927102759558",
                    'text':"Get ready for our spring flavor. Yum!"
                    },
                'total_retweets':"10",
                'total_likes':"10",
                'total_replies':"1",
                'replies':[
                    {
                        'tweet_id_str':"250075927172759552",
                        'created_at':"Sat May 06 03:35:21 +0000 2017",
                        'text':"@starbucks looking forward to your newest coffee.Love you",
                        'user':{
                            'name':"Thomas John Wakeman",
                            'user_id_str':"70789458",
                            'followers_count':"63",
                            'verified':"false"
                            }
                        }
                    ]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/communityengagement/overallengagement/get",methods=['GET'])
def getCommunityEngagemnetOverallEngagement():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'positive':["frapucino","starbucks"],
                'negative':["service","starbucks acai"]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/communityengagement/replyvalidity/get",methods=['GET'])
def getCommunityEngagementReplyValidity():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'positive':["frapucino","starbucks"],
                'negative':["service","starbucks acai"]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

@application.route("/api/v1/communityengagement/mentionvalidity/get",methods=['GET'])
def getCommunityEngagementMentionValidity():
    try:
        time_from=request.args.get('from')
        time_to=request.args.get('to')
        machineDetail = {
                'positive':["frapucino","starbucks"],
                'negative':["service","starbucks acai"]
                }
        return jsonify(machineDetail,time_from,time_to)
        #return jsonify(status='OK',message='hello vinda')
    except Exception as e:
        #return str(e)
        return jsonify(status='ERROR',message=str(e))

if __name__ == "__main__":
    application.run(host='0.0.0.0')

