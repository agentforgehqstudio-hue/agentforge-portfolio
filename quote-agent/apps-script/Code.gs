/**
 * Quote Agent (Google Apps Script, bound to a Google Sheet)
 *
 * Skeleton only. Implementation, prompts and settings removed in the public copy.
 */

// ---------------------------------------------------------------------------
// Settings
// ---------------------------------------------------------------------------

var MODEL; // value removed

var ANTHROPIC_URL; // value removed

var TABS; // value removed

var HEADERS; // value removed

var S; // value removed

var CAN_SEND; // value removed

var WATCH_REPLIES; // value removed

// ---------------------------------------------------------------------------
// Menu
// ---------------------------------------------------------------------------

function onOpen() {
  throw new Error('Implementation removed in the public copy.');
}

function setApiKey() {
  throw new Error('Implementation removed in the public copy.');
}

function setWebAppUrl() {
  throw new Error('Implementation removed in the public copy.');
}

function installTrigger() {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Setup: tabs, headers, demo business, demo price list, test cases
// ---------------------------------------------------------------------------

function setupSheet() {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Web endpoints
// ---------------------------------------------------------------------------

function doPost(e) {
  throw new Error('Implementation removed in the public copy.');
}

function doGet(e) {
  throw new Error('Implementation removed in the public copy.');
}

function approveFromPage(quoteId, token) {
  throw new Error('Implementation removed in the public copy.');
}

function saveEditFromPage(quoteId, token, form, sendNow) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Flow A: intake, draft, owner approval
// ---------------------------------------------------------------------------

function handleEnquiry_(enq) {
  throw new Error('Implementation removed in the public copy.');
}

function sendAck_(q, profile) {
  throw new Error('Implementation removed in the public copy.');
}

function draftAndNotify_(quoteId) {
  throw new Error('Implementation removed in the public copy.');
}

function sendOwnerEmail_(q, profile, draft) {
  throw new Error('Implementation removed in the public copy.');
}

function approveQuote_(quoteId, token) {
  throw new Error('Implementation removed in the public copy.');
}

function customerEmail_(q, profile, draft) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Claude: draft the estimate
// ---------------------------------------------------------------------------

function draftEstimate_(q, profile, prices) {
  throw new Error('Implementation removed in the public copy.');
}

var DRAFT_SCHEMA; // value removed

function validateDraft_(raw, prices) {
  throw new Error('Implementation removed in the public copy.');
}

function callClaude_(system, userText, schema, maxTokens) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Flow B: replies, STOP, follow-ups (runs every 5 minutes)
// ---------------------------------------------------------------------------

function tick() {
  throw new Error('Implementation removed in the public copy.');
}

function retryStuck_() {
  throw new Error('Implementation removed in the public copy.');
}

function checkReplies_() {
  throw new Error('Implementation removed in the public copy.');
}

function findReply_(email, since) {
  throw new Error('Implementation removed in the public copy.');
}

function stripQuoted_(text) {
  throw new Error('Implementation removed in the public copy.');
}

function isStopReply_(text) {
  throw new Error('Implementation removed in the public copy.');
}

function sendFollowUps_() {
  throw new Error('Implementation removed in the public copy.');
}

function sendFollowUp_(q, profile, n, hoursSince) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Testing helpers (menu)
// ---------------------------------------------------------------------------

function sendTestEnquiry() {
  throw new Error('Implementation removed in the public copy.');
}

function runTestCases() {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Parsing the form
// ---------------------------------------------------------------------------

function parseEnquiry_(body) {
  throw new Error('Implementation removed in the public copy.');
}

function tallyValue_(f) {
  throw new Error('Implementation removed in the public copy.');
}

function matchField_(label) {
  throw new Error('Implementation removed in the public copy.');
}

function parseLineItemsText_(text) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Pages (Approve / Edit)
// ---------------------------------------------------------------------------

function approvePage_(q, profile) {
  throw new Error('Implementation removed in the public copy.');
}

function editPage_(q, profile) {
  throw new Error('Implementation removed in the public copy.');
}

function page_(title, inner) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Email bits
// ---------------------------------------------------------------------------

function sendMail_(to, subject, html, profile) {
  throw new Error('Implementation removed in the public copy.');
}

function notifyAdmin_(subject, text) {
  throw new Error('Implementation removed in the public copy.');
}

function itemsTable_(items, cur) {
  throw new Error('Implementation removed in the public copy.');
}

function listBlock_(title, list, color) {
  throw new Error('Implementation removed in the public copy.');
}

function kv_(k, v) {
  throw new Error('Implementation removed in the public copy.');
}

function button_(href, label, color) {
  throw new Error('Implementation removed in the public copy.');
}

function money_(n, cur) {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Sheet helpers (columns are found by header name, so you can reorder them)
// ---------------------------------------------------------------------------

function sheet_(name) {
  throw new Error('Implementation removed in the public copy.');
}

function readTable_(name) {
  throw new Error('Implementation removed in the public copy.');
}

function appendObj_(name, obj) {
  throw new Error('Implementation removed in the public copy.');
}

function updateRow_(name, rowNum, patch) {
  throw new Error('Implementation removed in the public copy.');
}

function updateQuote_(rowNum, patch) {
  throw new Error('Implementation removed in the public copy.');
}

function findQuote_(quoteId) {
  throw new Error('Implementation removed in the public copy.');
}

function getProfile_(clientId) {
  throw new Error('Implementation removed in the public copy.');
}

function getPriceList_(clientId) {
  throw new Error('Implementation removed in the public copy.');
}

function log_(quoteId, event, detail) {
  throw new Error('Implementation removed in the public copy.');
}

function webAppUrl_() {
  throw new Error('Implementation removed in the public copy.');
}

// ---------------------------------------------------------------------------
// Small utilities
// ---------------------------------------------------------------------------

function now_() {
  throw new Error('Implementation removed in the public copy.');
}

function sumItems_(items) {
  throw new Error('Implementation removed in the public copy.');
}

function num_(v) {
  throw new Error('Implementation removed in the public copy.');
}

function norm_(s) {
  throw new Error('Implementation removed in the public copy.');
}

function firstName_(name) {
  throw new Error('Implementation removed in the public copy.');
}

function safeJson_(s) {
  throw new Error('Implementation removed in the public copy.');
}

function esc_(s) {
  throw new Error('Implementation removed in the public copy.');
}

function fmtDate_(d, tz) {
  throw new Error('Implementation removed in the public copy.');
}
